import json
import os

os.chdir(os.path.dirname(__file__))

ammo = {}
recipe = []


def fix(text):
    text = text.replace("forge:heads", "minecraft:skulls").replace("forge:glass_blocks_panes", "c:glass_panes").replace(
        "forge:leather", "c:leathers").replace("forge:gunpowder", "c:gunpowders").replace("forge:", "c:")
    text = {"c:glass": "c:glass_blocks",
            "c:glass/light_blue": "c:glass_panes"}.get(text, text)
    return text


for file in os.listdir("src/ammo"):
    path = os.path.join("src/ammo", file)
    with open(path, "r", encoding="utf-8") as fp:
        data = json.load(fp)
    item = []
    for value in data["materials"]:
        ret = {}
        if "count" in value:
            ret["count"] = value["count"]
        else:
            ret["count"] = 1
        material = value["item"]
        if "tag" in material:
            material["tag"] = fix(material["tag"])
        else:
            material["item"] = fix(material["item"])
        if "tag" in material:
            ret["basePredicate"] = {
                "tag": material["tag"]}
        else:
            ret["basePredicate"] = {"item": material["item"]}
        item.append(ret)
    ammo[f"tacz:ammo[custom_data={{AmmoId:'{data["result"]["id"]}'}}]"] = item
    if "tacz:" not in data["result"]["id"]:
        recipe.append(data)
with open("../kubejs/data/ammo.json", "w", encoding="utf-8")as fp:
    json.dump(
        dict(sorted(ammo.items(), key=lambda x: x[0])), fp, ensure_ascii=False)

for file in os.listdir("src/attachments"):
    path = os.path.join("src/attachments", file)
    with open(path, "r", encoding="utf-8") as fp:
        data = json.load(fp)
    for value in data["materials"]:
        material = value["item"]
        if "tag" in material:
            material["tag"] = fix(material["tag"])
        else:
            material["item"] = fix(material["item"])
    if "tacz:" not in data["result"]["id"]:
        recipe.append(data)

for file in os.listdir("src/gun"):
    path = os.path.join("src/gun", file)
    with open(path, "r", encoding="utf-8") as fp:
        data = json.load(fp)
    for value in data["materials"]:
        material = value["item"]
        if "tag" in material:
            material["tag"] = fix(material["tag"])
        else:
            material["item"] = fix(material["item"])
    if "tacz:" not in data["result"]["id"]:
        recipe.append(data)

with open("../kubejs/data/tacz.json", "w", encoding="utf-8")as fp:
    json.dump({"data": sorted(
        recipe, key=lambda x: ":".join([x["result"]["type"], *x["result"]["id"].split(":")]))}, fp, ensure_ascii=False)
