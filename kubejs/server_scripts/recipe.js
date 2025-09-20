ServerEvents.recipes(event => {
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
    // 深板岩圆石
    event.custom({
        "type": "create:compacting",
        "heat_requirement": "heated",
        "ingredients": [{
            "item": "minecraft:cobblestone"
        }, {
            "item": "minecraft:cobblestone"
        }, {
            "item": "minecraft:cobblestone"
        }, {
            "item": "minecraft:cobblestone"
        }, {
            "item": "minecraft:cobblestone"
        }, {
            "item": "minecraft:cobblestone"
        }, {
            "item": "minecraft:cobblestone"
        }, {
            "item": "minecraft:cobblestone"
        },
        ],
        "results": [
            {
                "id": "minecraft:cobbled_deepslate"
            }
        ]
    }).id("kjs/cobbled_deepslate")
    // 附魔金苹果
    event.shaped("minecraft:enchanted_golden_apple", ["GGG", "GAG", "GGG"], { G: "minecraft:gold_block", A: "minecraft:golden_apple" }).id("kjs/enchanted_golden_apple")
    // 原木箱子
    event.shaped("4x minecraft:chest", ["LLL", "L L", "LLL"], { L: "#minecraft:logs" }).id("kjs/chest")
    // 树皮锯锯末
    event.recipes.mekanismSawing("2x mekanism:sawdust", "4x farmersdelight:tree_bark").id("kjs/sawdust")
    // 量子缠绕态奇点复制
    // 尾缀`_manual_only`防止生成自动搅拌配方
    event.shapeless("2x ae2:quantum_entangled_singularity", ["ae2:singularity", "ae2:quantum_entangled_singularity"]).id("kjs/quantum_entangled_singularity_manual_only")
    // 门瑞欧树苗
    event.shapeless("integrateddynamics:menril_sapling", ["#minecraft:saplings", "integrateddynamics:menril_berries"]).id("kjs/menril_sapling")
    // 注液器与冶金灌注机联动
    event.forEachRecipe({ type: "mekanism:metallurgic_infusing" }, (recipe) => {
        let data = recipe.json
        let tag = String(data.get("chemical_input").get("tag")).slice(1, -1)
        let count = data.get("item_input").get("count")
        if (tag != "mekanism:bio" && tag != "mekanism:fungi" && (!count || count == 1)) {
            event.custom({
                "type": "create:filling",
                "ingredients": [
                    {
                        "type": "fluid_stack",
                        "amount": data.get("chemical_input").get("amount"),
                        "fluid": tag.replace("mekanism:", "kubejs:chemical/")
                    },
                    {
                        "item": data.get("item_input").get("item"),
                        "tag": data.get("item_input").get("tag")
                    }
                ],
                "results": [
                    {
                        "id": data.get("output").get("id")
                    }
                ]
            }).id(`kjs/${String(data.get("output").get("id")).slice(1, -1).split(":")[1]}`)
        }
    })
})

ItemEvents.crafted(event => {
    if (event.item == "ae2:quantum_entangled_singularity") {
        let data
        // 使用for循环而非直接getItems以兼容AE2合成终端
        for (let i = 0; i < 9; i++) {
            let item = event.getInventory().getItem(i)
            if (item.id == "ae2:quantum_entangled_singularity") {
                data = item.toJson()
                break
            }
        }
        if (data.has("components")) {
            // 是在找不到修改物品components的方法,用给玩家物品的方式实现
            event.item.copyAndClear()
            event.player.give(`2x ae2:quantum_entangled_singularity[ae2:entangled_singularity_id=${data.get("components").get("ae2:entangled_singularity_id")}L]`)
        }
    }
})
