import json
import os

os.chdir(os.path.dirname(__file__))

l = [i for i in os.listdir(".") if os.path.isdir(i)
     and i != "tacz_default_gun"]

ret = {}

TYPE = {
    "gun": "tacz:modern_kinetic_gun[custom_data={GunFireMode:'SEMI',GunId:'{id}'}]",
    "ammo": "tacz:ammo[custom_data={AmmoId:'{id}'}]",
    "attachment": "tacz:attachment[custom_data={AttachmentId:'{id}'}]"
}


def c(p):
    with open(p, "r", encoding="utf-8") as fp:
        data = json.load(fp)
    ingredients = []
    for i in data["materials"]:
        j = i["item"]
        if "tag" in j:
            j = {"tag": j["tag"].replace("forge:", "c:").replace("c:gunpowder", "c:gunpowders").replace("c:gunpowderss", "c:gunpowders").replace(
                "c:glass", "c:glass_blocks").replace(
                "c:glass_blocks_blocks", "c:glass_blocks").replace("c:glass_blocks_panes", "c:glass_panes").replace("c:heads", "minecraft:skulls")}
        c = i["count"] if "count" in i else 1
        ingredients.append({"basePredicate": j, "count": c})
    s = TYPE[data["result"]["type"]].replace(
        "{id}", data["result"]["id"])
    s = str(data["result"].get("count", 1))+"x "+s
    ret[s] = ingredients


for i in l:
    p = os.path.join(i, "data")
    p = os.path.join(p, os.listdir(
        p)[0], "recipe" if i == "tacz_default_gun" else "recipes")
    for i in os.listdir(p):
        pa = os.path.join(p, i)
        if os.path.isdir(pa):
            for i in os.listdir(pa):
                path = os.path.join(pa, i)
                c(path)

with open("../kubejs/tacz.json", "w", encoding="utf-8")as fp:
    json.dump(ret, fp, ensure_ascii=False)
