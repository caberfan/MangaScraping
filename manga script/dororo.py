import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

BASE = "https://dilib.vn/truyen-tranh/dororo-15836-chap-{}.html"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0",
})

for chap in range(1, 105):
    chapter_url = BASE.format(chap)

    print(f"\n=== Chapter {chap} ===")

    try:
        html = session.get(chapter_url, timeout=20).text
        soup = BeautifulSoup(html, "html.parser")

        images = []

        for img in soup.find_all("img"):
            src = img.get("src")

            if src and src.startswith("/img/comic/Dororo/"):
                images.append("https://dilib.vn" + src)

        if not images:
            print("No images found.")
            continue

        folder = f"Dororo/Chương {chap:03}"
        os.makedirs(folder, exist_ok=True)

        for i, image_url in enumerate(images):
            r = session.get(
                image_url,
                headers={"Referer": chapter_url},
                timeout=30,
            )

            if r.status_code == 200:
                filename = os.path.join(folder, f"{i:03}.jpg")

                img = Image.open(BytesIO(r.content))

                if img.mode != "RGB":
                    img = img.convert("RGB")

                img.save(filename, "JPEG", quality=95)

                print(f"Saved {filename}")
            else:
                print(f"Failed {image_url} ({r.status_code})")

    except Exception as e:
        print(f"Chapter {chap}: {e}")