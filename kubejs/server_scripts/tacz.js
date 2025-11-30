let ammo = JsonIO.read("kubejs/data/ammo.json")

ServerEvents.recipes(event => {
    // 沉浸工程自动化生产弹药
    for (let key in ammo) {
        event.custom({
            type: "immersiveengineering:blueprint",
            category: key.includes("tacz:") ? "bullet" : "specialBullet",
            result: Item.of(`tacz:ammo[custom_data={AmmoId:"${key}"}]`).toJson(),
            inputs: ammo[key]
        }).id(`kjs/tacz/ammo/${key.replace(":", "/")}`)
    }
})
