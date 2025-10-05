import subprocess
import json
import os

def download(url):
    image = curl(url, text = False)
    filename = "wallpapers/" + os.path.basename(url)

    with open(filename, "wb") as f:
        f.write(image)
    
    return filename

def fetch(url):
    data = json.loads(curl(url))

    output = {
        "date": data[0].get("date"),
        "title": data[0].get("title"),
        "copyright": data[0].get("copyright"),
        "image_url": data[0].get("fullUrl")
    }

    json_filename = "cache/data.json"
    with open(json_filename, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4, ensure_ascii=False)
    
    return output
        
def curl(url, text = True):
    return subprocess.run(
        ["curl", "-s", url],
        capture_output = True,
        text = text
    ).stdout

def main():
    data = fetch("https://peapix.com/bing/feed?country=us")
    filename = download(data["image_url"])

if __name__ == "__main__":
    main()
