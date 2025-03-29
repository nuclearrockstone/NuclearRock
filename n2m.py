import os
import requests
import time
import json
import hashlib

class NotionExporter:
    def __init__(self, token, database_id, version="2022-06-28",image_save_path="img"):
        self.token = token
        self.database_id = database_id
        self.version = version
        self.image_save_path = image_save_path
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": self.version,
            "Content-Type": "application/json"
        }

    def query_database(self):
        """查询数据库中的所有页面（支持分页）"""
        url = f"https://api.notion.com/v1/databases/{self.database_id}/query"
        has_more = True
        next_cursor = None
        results = []
        while has_more:
            payload = {"page_size": 100}
            if next_cursor:
                payload["start_cursor"] = next_cursor
            response = requests.post(url, headers=self.headers, json=payload)
            if response.status_code != 200:
                raise Exception(f"Query database error: {response.text}")
            data = response.json()
            results.extend(data.get("results", []))
            has_more = data.get("has_more", False)
            next_cursor = data.get("next_cursor")
            # 为防止速率限制，稍作延时
            time.sleep(0.2)
        return results

    def retrieve_block_children(self, block_id):
        """递归获取块的子块"""
        blocks = []
        url = f"https://api.notion.com/v1/blocks/{block_id}/children?page_size=100"
        has_more = True
        next_cursor = None
        while has_more:
            params = {}
            if next_cursor:
                params["start_cursor"] = next_cursor
            response = requests.get(url, headers=self.headers, params=params)
            if response.status_code != 200:
                raise Exception(f"Retrieve block children error: {response.text}")
            data = response.json()
            blocks.extend(data.get("results", []))
            has_more = data.get("has_more", False)
            next_cursor = data.get("next_cursor")
            time.sleep(0.2)
        return blocks

    def rich_text_to_markdown(self, rich_text_array):
        """将 Notion 的 rich_text 数组转换为 Markdown 文本，处理加粗、斜体、行内公式、行内代码块等格式"""
        texts = []
        for rt in rich_text_array:
            plain_text = rt.get("plain_text", "")
            if plain_text.startswith(":") and plain_text.endswith(":"):
                continue
            annotations = rt.get("annotations", {})
            # 处理加粗
            if annotations.get("bold"):
                plain_text = f"**{plain_text}**"
            # 处理斜体
            if annotations.get("italic"):
                plain_text = f"*{plain_text}*"
            # 处理行内代码块
            if annotations.get("code"):
                plain_text = f"`{plain_text}`"
            # 处理行内公式
            if rt.get("type") == "equation":
                plain_text = f"${plain_text}$"
            texts.append(plain_text)
        return "".join(texts)

    def block_to_markdown(self, block, indent=0, parentmd=""):
        """将单个块转换为 Markdown 格式，并递归处理子块"""
        md = ""
        block_type = block.get("type")
        content = block.get(block_type, {})
        prefix = "    " * indent  # 缩进用于嵌套块

        if block_type == "paragraph":
            md += prefix + self.rich_text_to_markdown(content.get("rich_text", [])) + "\n\n"
        elif block_type in ["heading_1", "heading_2", "heading_3"]:
            level = int(block_type.split("_")[1])
            md += prefix + "#" + ("#" * level) + " " + self.rich_text_to_markdown(content.get("rich_text", [])) + "\n\n"
            if block.get("has_children"):
                children = self.retrieve_block_children(block["id"])
                for child in children:
                    md += self.block_to_markdown(child, indent=indent, parentmd=md)
        elif block_type == "toggle":
            summary = self.rich_text_to_markdown(content.get("rich_text", []))
            md += prefix + f"<details>\n{prefix}<summary>{summary}</summary>\n\n"
            if block.get("has_children"):
                children = self.retrieve_block_children(block["id"])
                for child in children:
                    md += self.block_to_markdown(child, indent=indent+1, parentmd=md)
            md += prefix + "</details>\n\n"
        elif block_type == "code":
            language = content.get("language", "")
            code_text = self.rich_text_to_markdown(content.get("rich_text", []))
            indented_code_text = "\n".join([prefix + line for line in code_text.split("\n")])
            md += prefix + f"```{language}\n{indented_code_text}\n" + prefix + "```\n\n"
        elif block_type == "bookmark":
            url_text = content.get("url", "")
            caption = self.rich_text_to_markdown(content.get("caption", [])) or "Untitled Bookmark"
            md += prefix + f"[{caption}]({url_text})\n\n"
        elif block_type == "equation":
            expression = content.get("expression", "")
            md += prefix + f"$$ {expression} $$\n\n"
        elif block_type in ["bulleted_list_item", "numbered_list_item"]:
            if block_type == "numbered_list_item":
                lines = parentmd.strip().split("\n")
                if lines and lines[-1].strip().split(".")[0].isdigit():
                    last_number = int(lines[-1].strip().split(".")[0])
                    bullet = f"{last_number + 1}."
                else:
                    bullet = "1."
            else:
                bullet = "-"
            md += prefix + f"{bullet} {self.rich_text_to_markdown(content.get('rich_text', []))}\n"
            if block.get("has_children"):
                children = self.retrieve_block_children(block["id"])
                for child in children:
                    md += self.block_to_markdown(child, indent=indent+1, parentmd=md)
            md += "\n"
        elif block_type == "to_do":
            checked = content.get("checked", False)
            checkbox = "[x]" if checked else "[ ]"
            md += prefix + f"- {checkbox} {self.rich_text_to_markdown(content.get('rich_text', []))}\n\n"
        elif block_type == "child_page":
            title = block.get("child_page", {}).get("title", "Untitled")
            md += prefix + f"# {title}\n\n"
        elif block_type == "callout":
            icon = content.get("icon", {}).get("emoji", "")
            rich_text = self.rich_text_to_markdown(content.get("rich_text", []))
            md += prefix + f":::note {icon}\n\n{rich_text}\n\n"
            if block.get("has_children"):
                children = self.retrieve_block_children(block["id"])
                for child in children:
                    md += self.block_to_markdown(child, indent=indent+1, parentmd=md)
            md += prefix + "::: \n\n"
        elif block_type == "quote":
            md += prefix + f"> {self.rich_text_to_markdown(content.get('rich_text', []))}\n\n"
        elif block_type == "synced_block":
            synced_from = content.get("synced_from")
            if synced_from:
                original_block_id = synced_from.get("block_id")
                if original_block_id:
                    original_block = self.retrieve_block_children(original_block_id)
                    for child in original_block:
                        md += self.block_to_markdown(child, indent=indent, parentmd=md)
            else:
                if block.get("has_children"):
                    children = self.retrieve_block_children(block["id"])
                    for child in children:
                        md += self.block_to_markdown(child, indent=indent, parentmd=md)
        elif block_type == "table":
            table_width = content.get("table_width", 0)
            table_rows = self.retrieve_block_children(block["id"])
            if table_rows:
                header_row = table_rows[0]
                header_cells = header_row.get("table_row", {}).get("cells", [])
                header_md = "| " + " | ".join(self.rich_text_to_markdown(cell) for cell in header_cells) + " |\n"
                separator_md = "| " + " | ".join("---" for _ in header_cells) + " |\n"
                md += prefix + header_md + prefix + separator_md
                for row in table_rows[1:]:
                    cells = row.get("table_row", {}).get("cells", [])
                    row_md = "| " + " | ".join(self.rich_text_to_markdown(cell) for cell in cells) + " |\n"
                    md += prefix + row_md
                md += "\n"
        elif block_type == "image":
            image_url = content.get("external", {}).get("url") or content.get("file", {}).get("url")
            if image_url:
                # caption = " ".join([t.get("plain_text", "") for t in content.get("caption", [])])
                image_name = hashlib.md5(image_url.encode()).hexdigest()[:12]
                image_path = os.path.join(self.image_save_path, image_name)
                os.makedirs(self.image_save_path, exist_ok=True)
                response = requests.get(image_url)
            if response.status_code == 200:
                with open(image_path, "wb") as image_file:
                    image_file.write(response.content)
                    md += prefix + f"![{image_name}](/img/{image_name})\n\n"
            else:
                md += prefix + f"![{image_name}]({image_url})\n\n"
        else:
            md += prefix + f"*[{block_type} block not supported]*\n\n"
        return md

    def page_to_markdown(self, page):
        """将一个 Notion 页面转换为 Markdown 文本"""
        properties = page.get("properties", {})
        title = "Untitled"
        if "Name" in properties and properties["Name"]["title"]:
            title = "".join([t.get("plain_text", "") for t in properties["Name"]["title"]])
        md = f"# {title}\n\n"
        page_id = page["id"]
        blocks = self.retrieve_block_children(page_id)
        for block in blocks:
            md += self.block_to_markdown(block, parentmd=md)
        return md