import subprocess
import json
import os

def init(prefix_path):
    cmd = f'mkdir {prefix_path}/cache {prefix_path}/wallpapers &> /dev/null'
    subprocess.run(cmd, shell=True, executable="/bin/bash")
    
    cmd = f'touch {prefix_path}/cache/data.json'
    subprocess.run(cmd, shell=True, executable="/bin/bash")
    
def set_wallpaper(filename):
    cmd = 'gsettings set org.gnome.desktop.background picture-uri-dark "file://' + filename + '"'
    subprocess.run(cmd, shell=True, executable="/bin/bash", check=True)

def download(url, prefix_path):
    image = curl(url, text = False)
    filename = f"{prefix_path}/wallpapers/" + os.path.basename(url)

    with open(filename, "wb") as f:
        f.write(image)
    
    return filename

def fetch(url, prefix_path):
    data = json.loads(curl(url))

    output = {
        "date": data[0].get("date"),
        "title": data[0].get("title"),
        "copyright": data[0].get("copyright"),
        "image_url": data[0].get("fullUrl")
    }

    json_filename = f"{prefix_path}/cache/data.json"
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
    prefix_path = os.path.dirname(os.path.abspath(__file__))
    init(prefix_path)
    data = fetch("https://peapix.com/bing/feed?country=us", prefix_path)
    wallpaper = download(data["image_url"], prefix_path)
    set_wallpaper(wallpaper)
    print(data["title"])
    print(data["copyright"])

if __name__ == "__main__":
    main()
