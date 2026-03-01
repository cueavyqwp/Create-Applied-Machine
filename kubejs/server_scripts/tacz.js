ServerEvents.recipes(event => {
    // 沉浸工程自动化生产弹药
    event.forEachRecipe({ type: "tacz:gun_smith_table_crafting" }, (recipe) => {
        if (String(recipe.json.get("result").get("type")).slice(1, -1) == "ammo") {
            let data = []
            let key = String(recipe.json.get("result").get("id")).slice(1, -1)
            recipe.json.get("materials").forEach((value) => {
                data.push({
                    "count": value.get("count") ?? 1,
                    "basePredicate": value.get("item")
                })
            })
            event.custom({
                type: "immersiveengineering:blueprint",
                category: key.includes("tacz:") ? "bullet" : "specialBullet",
                result: Item.of(`tacz:ammo[custom_data={AmmoId:"${key}"}]`).toJson(),
                inputs: data
            }).id(`kjs/tacz/ammo/${key.replace(":", "/")}`)
        }
    })
})
