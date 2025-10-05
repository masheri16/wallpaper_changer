import subprocess
import json

def fetch(url):
    data = json.loads(curl(url).stdout)

    output = {
        "date": data[0].get("date"),
        "title": data[0].get("title"),
        "copyright": data[0].get("copyright"),
        "image_url": data[0].get("fullUrl")
    }

    json_filename = "cache/data.json"
    with open(json_filename, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4, ensure_ascii=False)
        
def curl(url):
    return subprocess.run(
        ["curl", "-s", url],
        capture_output = True,
        text = True
    )

def main():
    fetch("https://peapix.com/bing/feed?country=us")

if __name__ == "__main__":
    main()
