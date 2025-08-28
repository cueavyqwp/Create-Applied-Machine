
__version__ = "0.0.2"

skip = (".git", ".github", "__pycache__", ".gitignore",
        "export_config.txt", "README.md", "cover.py", "update.py")

if __name__ == "__main__":
    import zipfile
    import shutil
    import os

    home = os.path.dirname(__file__)
    os.chdir(home)

    if os.path.isfile("1.21.1-Create.jar"):
        print("检测在本地,跳过打包")
        exit()

    os.mkdir("./dist")
    os.makedirs("./output/overrides")
    shutil.move("./src/modrinth.index.json", "./output/modrinth.index.json")
    shutil.move("./src/CHANGELOG.md", "./output/CHANGELOG.md")
    shutil.move("./src/LICENSE", "./output/LICENSE")
    for path in os.listdir("./src"):
        if path in skip:
            continue
        path = os.path.join("./src", path)
        shutil.move(path, f"./output/overrides/{os.path.basename(path)}")
    with zipfile.ZipFile(f"./dist/1.21.1-Create-{__version__}.zip", "w") as zf:
        os.chdir("./output")
        for root, _, files in os.walk("."):
            for file in files:
                if file in skip:
                    continue
                zf.write(os.path.join(root, file))
