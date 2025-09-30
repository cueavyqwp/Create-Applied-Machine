let ammo = JsonIO.read("kubejs/data/ammo.json")
let tacz = JsonIO.read("kubejs/data/tacz.json")
let num = 0

ServerEvents.recipes(event => {
    // 沉浸工程自动化生产弹药
    for (let key in ammo) {
        let category = key.includes("tacz:") ? "bullet" : "specialBullet"
        event.custom({
            type: "immersiveengineering:blueprint",
            category: category,
            result: Item.of(`tacz:ammo[custom_data={AmmoId:'{${ammo[key]}}'}]`).toJson(),
            inputs: ammo[key]
        }).id(`kjs/tacz/${num}`)
        num++
    }
    // js限制,不允许JSON文件最外层必须是数组
    for (let key in tacz["data"]) {
        console.log(tacz["data"][key]["materials"])
        event.custom(tacz["data"][key]).id(`kjs/tacz/${num}`)
        num++
    }
})
