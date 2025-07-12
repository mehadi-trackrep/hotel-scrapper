import subprocess
import json
import tempfile
import os
from typing import List

async def run_spiders(city: str) -> List[dict]:
    results = []

    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp_file:
        output_path = tmp_file.name

    try:
        for spider in ["booking", "agoda"]:
            subprocess.run([
                "scrapy", "crawl", spider,
                "-a", f"city={city}",
                "-o", output_path,
                "-t", "json"
            ], check=True)

        with open(output_path) as f:
            results = json.load(f)

    except Exception as e:
        print("Scraping error:", e)

    finally:
        os.remove(output_path)

    return results
