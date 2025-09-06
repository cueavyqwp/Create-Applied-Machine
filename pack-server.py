if __name__ != "__main__":
    exit()

import pack

__version__ = pack.__version__

import zipfile
import os

need = (
    "rhino",
    "jupiter",
    "yungsapi",
    "patchouli"
)

skip = (
    "colorwheel",
    "extremeSoundmuffler",
    "fullbrightnesstoggle",
    "probejs",
    "searchables",
    "skinlayers3d",
    "kubejsoffline",
    "wi-zoom",
    "cherishedworlds",
    "notenoughanimations",
    "catalogue",
    "toastcontrol",
    "modernui",
    "realcamera",
    "0pack2reload",
    "configured",
    "sodiumdynamiclights"
)

os.chdir(os.path.dirname(__file__))

target = []

for name in os.listdir("mods"):
    if any(True for item in skip if item in name.lower()):
        continue
    path = os.path.join("mods", name)
    keep = False
    if any(True for item in need if item in name.lower()):
        keep = True
    else:
        with zipfile.ZipFile(path, "r") as zf:
            if "META-INF/neoforge.mods.toml" not in zf.namelist():
                continue
            for line in zf.read("META-INF/neoforge.mods.toml").decode("utf-8").splitlines():
                line = line.strip().lower()
                if not line.startswith("side"):
                    continue
                side = line.partition(
                    "=")[-1].strip().replace("'", "\"").split("\"")[1]
                if side == "client":
                    break
                elif side == "both" or side == "server":
                    keep = True
                    break
    if not keep:
        continue
    target.append(path)
    print(f"模组: {name}")

for root, _, files in os.walk("config"):
    for file in files:
        path = os.path.join(root, file)
        if "client" in file or ".bak" in file or ".md" in file or "iris" in file or "jech" in file or "catalogue" in file or "cache" in path or "jei" in path or "jade" in path or "NoChatReports" in path:
            continue
        print(f"配置: {path}")
        target.append(path)

for root, _, files in os.walk("kubejs"):
    for file in files:
        path = os.path.join(root, file)
        if "documentation" in path or "README" in path or "client_scripts" in path or ("startup_scripts" in path and file == "tacz.js"):
            continue
        print(f"魔改: {path}")
        target.append(path)

for file in os.listdir("tacz"):
    path = os.path.join("tacz", file)
    if os.path.isfile(path) and os.path.splitext(file)[-1] == ".zip":
        print(f"枪包: {file}")
        target.append(path)

print("导出至dist文件夹")
with zipfile.ZipFile(f"./dist/1.21.1-Create-server-{__version__}.zip", "w") as zf:
    for path in target:
        zf.write(path)
print("完成!")
