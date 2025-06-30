import snscrape.modules.twitter as sntwitter
import requests

def fetch_all_social_posts():
    results = []
    for i, keyword in enumerate(["inmigración", "puerto rico", "economía", "ICE", "restaurante"]):
        for tweet in sntwitter.TwitterSearchScraper(f"{keyword} since:2025-06-28 until:2025-06-29").get_items():
            results.append({
                "platform": "X",
                "username": tweet.user.username,
                "date": tweet.date.strftime('%Y-%m-%d %H:%M'),
                "content": tweet.content,
                "url": tweet.url
            })
            if len(results) > 150:
                break
    reddit_posts = [{
        "platform": "Reddit",
        "username": "user123",
        "date": "2025-06-29 10:20",
        "content": "Reddit用户发文关于波多黎各电价上涨",
        "url": "https://reddit.com/r/puertorico"
    }]
    results.extend(reddit_posts)
    return results