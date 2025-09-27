import typing

name: str = "Create: Applied Machine"
id: str = name.replace(": ", "-").replace(" ", "-")
summary: str = "机械动力: 应用机器"
version: str = "0.1.1"

out: str = f"{id}-{version}.zip"
out_server: str = f"{id}-{version}-server.zip"

version_mc: str = "1.21.1"
loader: typing.Literal["forge", "neoforge", "fabric-loader"] = "neoforge"
loader_version = "21.1.209"

files_append: list[dict[str, typing.Any]] = [
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
    },
    {
        "path": "resourcepacks/3D-Default.zip",
        "hashes": {
                "sha1": "94af4e0f831dcf2ca84f2dd92919da6a04da4bb6",
                "sha512": "24834da3945db195bfc57932fde4a22a062d14718bda3eece666778e02b1c6b0200edf3c9a25f4ae2760fccc7db7bfd498dc3479a3f7a330b33867fd5ac6fe8f"
        },
        "downloads": [
            "https://cdn.modrinth.com/data/5aPp18Lx/versions/QkY0fhSG/3D%20Default%201.20%2B%20v1.12.0.zip"
        ],
        "fileSize": 856491
    },
    {
        "path": "resourcepacks/Borderless-Glass.zip",
        "hashes": {
                "sha1": "0e64157157dd39936164f7f201284e306f6a59d4",
                "sha512": "6d433c65233ee5fb7b38b9eef33f10d448f0397238cbf7e28383d1566992a9cf83584cffed0338b535863388a12cf87d32e0b3e60f9431e596e14896ab0a7717"
        },
        "downloads": [
            "https://cdn.modrinth.com/data/1Ja8Sg6j/versions/AaBDFaRI/Borderless%2BGlass%2Bv1.0%28mc-1.21%29.zip"
        ],
        "fileSize": 20766
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
