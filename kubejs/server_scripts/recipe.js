ServerEvents.recipes(event => {
    // 曲柄之间互换
    event.shapeless("create:hand_crank", ["ae2:crank"]).id("kjs/crank/0")
    event.shapeless("create:hand_crank", ["supplementaries:crank"]).id("kjs/crank/1")
    event.shapeless("ae2:crank", ["create:hand_crank"]).id("kjs/crank/2")
    event.shapeless("ae2:crank", ["supplementaries:crank"]).id("kjs/crank/3")
    event.shapeless("supplementaries:crank", ["ae2:crank"]).id("kjs/crank/4")
    event.shapeless("supplementaries:crank", ["create:hand_crank"]).id("kjs/crank/5")
    // 书
    event.shapeless("minecraft:book", ["#minecraft:bookshelf_books"]).id("kjs/book/0")
    event.shapeless("minecraft:book", ['patchouli:guide_book[patchouli:book="touhou_little_maid:memorizable_gensokyo"]']).id("kjs/book/1")
    event.shapeless("minecraft:book", ['patchouli:guide_book[patchouli:book="modularrouters:book"]']).id("kjs/book/2")
    event.shapeless("minecraft:book", ["ae2:guide"]).id("kjs/book/3")
    // 鞍
    event.shaped("minecraft:saddle", [" L ", "LIL"], { L: "minecraft:leather", I: "#c:ingots/iron" }).id("kjs/saddle")
    // 半砖合木板
    Ingredient.of("#minecraft:wooden_slabs").stacks.forEach(stack => {
        let id = stack.getId()
        let ret = null
        if (id == "youkaishomecoming:hay_slab") {
            ret = "minecraft:hay_block"
        } else if (id == "youkaishomecoming:straw_slab") {
            ret = "farmersdelight:straw_bale"
        } else {
            ret = id.replace("_slab", "_planks")
        }
        event.shaped(ret, [" S", " S"], { S: id }).id(`kjs/planks/${id.split(":")[1].split("_slab")[0]}`)
    })
    // 紫水晶
    event.shapeless("4x minecraft:amethyst_shard", ["minecraft:amethyst_block"]).id("kjs/amethyst")
    // 红色染料
    event.shapeless("minecraft:red_dye", ["minecraft:redstone"]).id("kjs/red_dye")
    // 龙蛋再生
    event.shapeless("2x minecraft:dragon_egg", ["minecraft:dragon_egg", "draconicevolution:dragon_heart"]).id("kjs/dragon_egg")
})