import typing

name: str = "Create: Applied Machine"
id: str = name.replace(": ", "-").replace(" ", "-")
summary: str = "机械动力: 应用机器"
version: str = "0.0.7"

out: str = f"{id}-{version}.zip"
out_server: str = f"{id}-{version}-server.zip"

version_mc: str = "1.21.1"
loader: typing.Literal["forge", "neoforge", "fabric-loader"] = "neoforge"
loader_version = "21.1.209"

files_append: list[dict[str, typing.Any]] = [
    {
        "path": "mods/tacz-neoforge-1.21.1-1.1.6-hotfix-r5.jar",
        "hashes": {
                "sha1": "c4ea60bf4d76716e7e3a7b2f22eb2ab338df51a3",
                "sha512": "c28a8a6137c4e89770c57a2251a21adae228609f7b757d18ce3958bc0325900e91d6a4b1eef44eaecab56d24dad120e0639b6dcda2f656d9a7a9df8c61df4e3d"
        },
        "downloads": [
            "https://github.com/MUKSC/TACZ-1.21.1/releases/download/neoforge-1.1.6-hotfix-r5/tacz-neoforge-1.21.1-1.1.6-hotfix-r5.jar"
        ],
        "fileSize": 47612775
    },
    {
        "path": "shaderpacks/BSL_v10.0.zip",
        "hashes": {
                "sha1": "82eb9981a31a4753bb5022b5f64d5ec4f6a27071",
                "sha512": "3ce31ae8c7242ae335de70df10f8147420a64ca372585c195d0b300f9e8c5b923f1e5bf2b8dddfcc741a0ce8e0235e079540101632837624787da84e9b52d72f"
        },
        "downloads": [
            "https://cdn.modrinth.com/data/Q1vvjJYV/versions/jRn8y2VF/BSL_v10.0.zip"
        ],
        "fileSize": 1121678
    }
]

if __name__ == "__main__":
    import zipfile
    import json
    import os

    src = f"{id}.zip"
    if not os.path.isfile(src):
        print(f"文件: '{src}' 未找到,请先使用PCL2导出整合包")

    with zipfile.ZipFile(src, "r") as zf:
        data = json.loads(zf.read("modrinth.index.json"))

    data["name"] = name
    data["summary"] = summary
    data["versionId"] = version
    data["files"] += files_append

    with open("modrinth.index.json", "w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=4)

    print(f"文件: 'modrinth.index.json' 已更新")

# 仅从modrinth上获取模组不全
if False and __name__ == "__main__":
    import hashlib
    import json
    import os

    import requests

    os.chdir(os.path.dirname(__file__))

    data = {
        "game": "minecraft",
        "formatVersion": 1,
        "versionId": version,
        "name": name,
        "summary": summary,
        "dependencies": {
            "minecraft": version_mc,
            loader: loader_version
        },
        "files": []
    }
    if not os.path.isfile("cache.json"):
        cache = {}
    else:
        with open("cache.json", "r", encoding="utf-8") as fp:
            cache = json.load(fp)
    for name in os.listdir("mods"):
        path = os.path.join("mods", name)
        with open(path, "rb") as fp:
            sha1 = hashlib.sha1(fp.read()).hexdigest()
        if sha1 not in cache:
            response = requests.get(
                f"https://api.modrinth.com/v2/version_file/{sha1}")
            if not response.ok:
                print(f"[{name}]({sha1}) pass [{response.status_code}]")
                continue
            files = response.json()["files"][0]
            cache[sha1] = {"path": f"mods/{name}", "hashes": files,
                           "downloads": [files["url"]], "fileSize": files["size"]}
        data["files"].append(cache[sha1])
        print(f"[{name}]({sha1}) OK!")
    data["files"] += files_append
    with open("cache.json", "w", encoding="utf-8") as fp:
        json.dump(cache, fp, indent=4, ensure_ascii=False)
    with open("modrinth.index.json", "w", encoding="utf-8") as fp:
        json.dump(data, fp, indent=4, ensure_ascii=False)
