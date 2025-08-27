let data = JsonIO.read("kubejs/tacz.json")
let skip = [43, 188]
ServerEvents.recipes(event => {
    let num = 0
    for (let key in data) {
        if (skip.includes(num)) {
            num++
            continue
        }
        event.custom({
            type: "immersiveengineering:blueprint",
            category: "specialBullet",
            result: Item.of(key).toJson(),
            inputs: data[key]
        }).id(`kjs/tac/${num}`)
        num++
    }
})