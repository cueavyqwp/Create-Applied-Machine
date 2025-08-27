ServerEvents.recipes(event => {
    let i = 114514
    Ingredient.of("#c:raw_materials").stacks.forEach(stack => {
        let id = stack.getId()
        let name = stack.getDisplayName().getString()
        let key = id.split(":")[1]
        if (!(id.startsWith("minecraft:") || id.startsWith("twilightforest:"))) {
            event.recipes.createoreexcavation.vein({ "text": name }, id).placement(32, 4, i).id(`kubejs:vein/${key}`).biomeWhitelist('minecraft:is_overworld')
            event.recipes.createoreexcavation.drilling(id, `kubejs:vein/${key}`, 600).id(`kjs/drilling/${key}`)
            i++
        }
    })
})