ClientEvents.tick(event => {
    let player = event.player
    if (player.stages.has("night_vision") && !player.hasEffect("minecraft:night_vision")) {
        player.potionEffects.add("minecraft:night_vision", -1, 255, false, false);
    }
})
