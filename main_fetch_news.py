from modules.fetch_news import fetch_news_articles
from modules.ai_select import select_top_posts
from modules.export_excel import export_to_excel

if __name__ == "__main__":
    all_articles = fetch_news_articles()
    top_articles = select_top_posts(all_articles, top_k=30)
    export_to_excel(top_articles, "./output/2025-06-30/news_top30.xlsx")