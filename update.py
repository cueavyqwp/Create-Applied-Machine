import pack

import zipfile
import json
import os

os.chdir(os.path.dirname(__file__))

src = "1.21.1-Create.zip"
out = "modrinth.index.json"

if not os.path.isfile(src):
    print(f"文件: '{src}' 未找到,请先使用PCL2导出整合包")

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

with zipfile.ZipFile(src, "r") as zf:
    data = json.loads(zf.read("modrinth.index.json"))

data["versionId"] = pack.__version__
data["summary"] = "1.21.1-Create"
data["files"] += files

with open(out, "w", encoding="utf-8") as fp:
    json.dump(data, fp, ensure_ascii=False, indent=4)

print(f"文件: '{out}' 已更新")
