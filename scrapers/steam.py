import requests
import os
from dotenv import load_dotenv

load_dotenv()

class SteamScraper:
    def __init__(self):
        pass

    
    def fetch(self, game_id, num_reviews=100):
        url = f"https://store.steampowered.com/appreviews/{game_id}?json=1&num={num_reviews}"
        response = requests.get(url)
        data = response.json()
        reviews = data["reviews"]
        total_positive = data["query_summary"]["total_positive"]
        results = []
        for r in reviews:
            text = r["review"]
            rating = r["voted_up"]
            playtime_forever = r["author"]["playtime_forever"]
            votes_funny= r["votes_funny"]
            timestamp_created = r["timestamp_created"]
            steamid = r["author"]["steamid"]
            results.append({"text": text,"rating": rating,"playtime_forever": playtime_forever,
                            "votes_funny": votes_funny,
                            "timestamp_created": timestamp_created,
                            "steamid": steamid,
                            "total_positive": total_positive}
                            )
        return results

Scraper=SteamScraper()
reviews=Scraper.fetch("1245620")
print(reviews[1])