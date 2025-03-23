import os
import json
import requests
from n2m import NotionExporter

class DocusaurusPostGenerator:
    def __init__(self, token, database_id, output_dir="blog"):
        self.notion_exporter = NotionExporter(token, database_id, image_save_path="blog/static/img")
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_posts(self):
        pages = self.notion_exporter.query_database()
        for page in pages:
            md_content = self.notion_exporter.page_to_markdown(page)
            properties = page.get("properties", {})
            slug = properties.get("Slug", {}).get("rich_text", [{}])[0].get("plain_text", "untitled")
            tags = [tag.get("name").replace("'","") for tag in properties.get("Tags", {}).get("multi_select", [])]
            truncate_marker = "<!--truncate-->"
            truncated_content = md_content.split("\n\n", 2)[1] + "\n\n" + truncate_marker + "\n\n" + md_content.split("\n\n", 2)[2]

            front_matter = {
                "slug": slug,
                "title": properties.get("Name", {}).get("title", [{}])[0].get("plain_text", "Untitled"),
                "tags": tags
            }

            front_matter_str = "\n".join([f"{key}: {value}" for key, value in front_matter.items()])
            post_content = "---\n" + front_matter_str + "\n---\n\n" + truncated_content

            created_time = page.get("created_time", "1970-01-01T00:00:00.000Z")
            created_date = created_time.split("T")[0]
            filename = f"{created_date}-{slug}.md"
            with open(os.path.join(self.output_dir, filename), "w", encoding="utf-8") as f:
                f.write(post_content)

if __name__ == "__main__":
    token = os.getenv("NOTION_TOKEN")
    database_id = os.getenv("BLOG_DATABASE_ID")
    generator = DocusaurusPostGenerator(token, database_id)
    generator.generate_posts()