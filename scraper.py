import asyncio
import httpx
from bs4 import BeautifulSoup
import json

class BusinessScraper:
    def __init__(self, start_id, end_id, output_file="raw_data.jsonl"):
        self.start_id = start_id
        self.end_id = end_id
        self.output_file = output_file
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    async def fetch_id(self, client, cid):
        url = f"https://www.e-register.am/am/companies/{cid}"
        try:
            resp = await client.get(url, timeout=10)
            if resp.status_code == 200:
                return {"id": cid, "html": resp.text}
            return None
        except Exception:
            return None

    async def run(self):
        async with httpx.AsyncClient(headers=self.headers) as client:
            curr = self.start_id
            while curr < self.end_id:
                tasks = [self.fetch_id(client, cid) for cid in range(curr, curr + 25)]
                results = await asyncio.gather(*tasks)
                for res in results:
                    if res:
                        with open(self.output_file, 'a', encoding='utf-8') as f:
                            f.write(json.dumps(res, ensure_ascii=False) + "\n")
                curr += 25
                print(f"Scanned up to ID: {curr}")

if __name__ == "__main__":
    scraper = BusinessScraper(start_id=1561192, end_id=1562000)
    asyncio.run(scraper.run())