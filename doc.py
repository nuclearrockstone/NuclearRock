from n2m import NotionExporter
import os
import shutil

# 配置 Notion API 令牌和数据库 ID
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTE_DATABASE_ID")

# 初始化 NotionExporter
exporter = NotionExporter(NOTION_TOKEN, DATABASE_ID,image_save_path="docs/static/img")

# 查询数据库中的所有页面
pages = exporter.query_database()

# 导出目录
export_dir = "docs/note"
os.makedirs(export_dir, exist_ok=True)

# 遍历每个页面并导出为 Markdown 文件
for page in pages:
    properties = page.get("properties", {})
    publish_property = properties.get("Publish", {})
    if publish_property.get("type") == "checkbox" and publish_property.get("checkbox"):
        title = "Untitled"
        if "Name" in properties and properties["Name"]["title"]:
            title = "".join([t.get("plain_text", "") for t in properties["Name"]["title"]])
        sidebar_position = properties.get("sidebar_position", {}).get("number", None)
        front_matter = {
            "title": title,
            "sidebar_position": sidebar_position
        }
        md_content = "---\n"
        for key, value in front_matter.items():
            if value is not None:
                md_content += f"{key}: {value}\n"
        md_content += "---\n\n" + exporter.page_to_markdown(page)
        file_path = os.path.join(export_dir, f"{title}.md")
        category = ""
        if "Category" in properties and properties["Category"]["select"]:
            category = properties["Category"]["select"]["name"]
        category_dir = os.path.join(export_dir, category) if category else export_dir
        os.makedirs(category_dir, exist_ok=True)
        file_path = os.path.join(category_dir, f"{title}.md")
        with open(file_path, "w", encoding="utf-8") as md_file:
            md_file.write(md_content)
        print(f"Exported: {file_path}")
