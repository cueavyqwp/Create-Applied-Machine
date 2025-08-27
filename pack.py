
__version__ = "0.0.1"

if __name__ != "__main__":
    exit()

import requests

import zipfile
import shutil
import json
import os

os.chdir(os.path.dirname(__file__))

if os.path.isfile("1.21.1-Create.jar"):
    src = "1.21.1-Create.zip"
    out = "modrinth.index.json"

    files = [
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
        }
    ]

    if not os.path.isfile(src):
        print(f"文件: '{src}' 未找到,请先使用PCL2导出整合包")

    with zipfile.ZipFile(src, "r") as zf:
        data = json.loads(zf.read("modrinth.index.json"))

    data["versionId"] = __version__
    data["summary"] = "1.21.1-Create"
    data["files"] += files

    with open(out, "w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=4)

    print(f"文件: '{out}' 已更新")

else:
    if not os.path.isdir("mods"):
        os.mkdir("mods")

    if not os.path.isfile("mods/tiabcurio-neoforge-1.21.1-3.0.1.jar"):
        with open("mods/tiabcurio-neoforge-1.21.1-3.0.1.jar", "wb") as fp:
            fp.write(requests.get(
                "https://mediafilez.forgecdn.net/files/6109/580/tiabcurio-neoforge-1.21.1-3.0.1.jar").content)

    os.mkdir("dist")
    os.mkdir("output")
    os.mkdir("output/overrides")
    shutil.move("modrinth.index.json", "output/modrinth.index.json")
    for path in os.listdir():
        if path not in (".github", "pack.py", ".gitignore", "export_config.txt"):
            (shutil.copy, shutil.copytree)[os.path.isdir(path)](path, "output/overrides" +
                                                                "" if os.path.isfile(path)else f"/{path}")
    with zipfile.ZipFile(f"dist/1.21.1-Create-{__version__}.zip", "w") as zf:
        for root, _, files in os.walk("output"):
            for file in files:
                zf.write(os.path.join(root, file))
