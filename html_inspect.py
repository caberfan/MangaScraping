import requests

url = "https://dilib.vn/truyen-tranh/lang-khach-vagabond-5566-chap-356.html"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

with open("page.html", "w", encoding="utf-8") as f:
    f.write(html)