
__version__ = "0.0.3"

skip = (".gitignore", "export_config.txt",
        "README.md", "cover.py", "update.py")

if __name__ == "__main__":
    import zipfile
    import os

    os.chdir(os.path.dirname(__file__))

    if os.path.isfile("1.21.1-Create.jar"):
        import subprocess
        print("改用本地打包方式")
        os.mkdir("./dist")
        with zipfile.ZipFile(f"./dist/1.21.1-Create-{__version__}.zip", "w") as zf:
            for path in subprocess.run(("git", "ls-files"), capture_output=True, text=True, check=True).stdout.strip().split("\n"):
                # 简化打包内容
                if ".github" in path or ".gitignore" in path or "LICENSE" in path or ".md" in path in path or ".py" in path or "export_config.txt" in path:
                    continue
                zf.write(path, None if path == "modrinth.index.json" else os.path.join(
                    "overrides", path))
    else:
        import pathlib
        import shutil
        os.mkdir("./dist")
        os.mkdir("./output")
        shutil.move("./src/modrinth.index.json",
                    "./output/modrinth.index.json")
        shutil.move("./src/CHANGELOG.md", "./output/CHANGELOG.md")
        shutil.move("./src/LICENSE", "./output/LICENSE")
        for root, _, files in os.walk("./src"):
            if ".git" in root or ".github" in root or "__pycache__" in root:
                continue
            for file in files:
                if file in skip:
                    continue
                path = os.path.join(root, file)
                to = pathlib.Path().joinpath(*pathlib.Path(path).parts[1:])
                os.makedirs(os.path.dirname(to), exist_ok=True)
                shutil.move(path, os.path.join(
                    "./output/overrides", to))
