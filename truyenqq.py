import os
import requests
from bs4 import BeautifulSoup

BASE = "https://truyenqq.com.vn/monster-deluxe-edition/chapter-{}"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0",
})

for chap in range(1, 2):  # Chapters 1-162
    chapter_url = BASE.format(chap)

    print(f"\n=== Chapter {chap} ===")

    try:
        html = session.get(chapter_url, timeout=20).text
        soup = BeautifulSoup(html, "html.parser")

        images = [
            img["data-src"]
            for img in soup.select("img.lazy")
            if img.get("data-src")
        ]

        if not images:
            print("No images found.")
            continue

        folder = f"Monster Deluxe Edition/Chapter {chap:03}"
        os.makedirs(folder, exist_ok=True)

        for i, image_url in enumerate(images):
            r = session.get(
                image_url,
                headers={"Referer": chapter_url},
                timeout=30,
            )

            if r.status_code == 200:
                filename = os.path.join(folder, f"{i:03}.jpg")
                with open(filename, "wb") as f:
                    f.write(r.content)
                print(f"Saved {filename}")
            else:
                print(f"Failed {image_url} ({r.status_code})"

)

    except Exception as e:
        print(f"Chapter {chap}: {e}")