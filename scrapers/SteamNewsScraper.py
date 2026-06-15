import re
import requests
import time

class SteamNewsScraper:
    def __init__(self):
        self.base_url = "https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/"
        self.game_ids = {
    "elden_ring": "1245620",
    "cyberpunk": "1091500",
    "hogwarts_legacy": "990080",
    "baldurs_gate3": "1086940"
}
    def fetch(self, game_name, num_posts=100):
        appid = self.game_ids[game_name.lower().replace(" ", "_")]
        if not appid:
            raise ValueError(f"Game '{game_name}' not found in game IDs.")

        params = {
            "appid": appid,
            "count": num_posts
        }
        response = requests.get(self.base_url, params=params)

        data = response.json()
        posts = data["appnews"]["newsitems"]
        results = []
        for post in posts:

            content = post["contents"]
            content = re.sub(r'<.*?>', '', content)
            author = post["author"]
            title = post["title"]
            id= post["gid"]
            date= post["date"]
            created_utc = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(date))
           
            results.append({
                "id": id,
                "title": title,
                "content": content,
                "author": author,
                "created_utc": created_utc
            })
        return results
    
Scraper = SteamNewsScraper()
reviews = Scraper.fetch("Elden Ring", num_posts=10)
print(reviews[0])