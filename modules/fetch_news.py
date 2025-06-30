import feedparser

def fetch_news_articles():
    feeds = [
        "https://www.elnuevodia.com/rss/ultimas-noticias/",
        "https://www.metro.pr/rss",
        "https://www.noticel.com/rss"
    ]
    articles = []
    for url in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            articles.append({
                "platform": "News",
                "username": entry.get("source", {}).get("title", ""),
                "date": entry.published,
                "content": entry.title + " " + entry.summary,
                "url": entry.link
            })
    return articles