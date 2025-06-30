from modules.fetch_social import fetch_all_social_posts
from modules.ai_select import select_top_posts
from modules.export_excel import export_to_excel

if __name__ == "__main__":
    all_posts = fetch_all_social_posts()
    top_posts = select_top_posts(all_posts, top_k=30)
    export_to_excel(top_posts, "./output/2025-06-30/social_top30.xlsx")