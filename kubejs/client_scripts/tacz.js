// 近战武器列表(GunId)
const meleeWeapons = ["applied_armorer:special_melee_task_manager", "create_armorer:special_melee_wrench"]
ClientEvents.tick(event => {
    let specKey = global.meleeSpecKey
    let player = event.player
    // 只要处于按下状态都会触发,若只想判断按下那次则改用 specKey.consumeClick()
    if (specKey.isDown()) {
        let item = player.getMainHandItem()
        if (item.id != "tacz:modern_kinetic_gun") return
        // 这id终于让我给找到了
        let id = item.getCustomData()["GunId"].getAsString()
        if (meleeWeapons.includes(id)) {
            player.melee()
        }
    }
})
