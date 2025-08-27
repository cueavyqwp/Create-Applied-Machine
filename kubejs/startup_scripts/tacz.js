// 参考自: https://www.mcmod.cn/post/4556.html
const $KeyMapping = Java.loadClass("net.minecraft.client.KeyMapping");
const $IKeyConflictContext = Java.loadClass("net.neoforged.neoforge.client.settings.IKeyConflictContext");
const $KeConflictContext = Java.loadClass("net.neoforged.neoforge.client.settings.KeyConflictContext");
const $KeyModifier = Java.loadClass("net.neoforged.neoforge.client.settings.KeyModifier");
const $InputConstantsType = Java.loadClass("com.mojang.blaze3d.platform.InputConstants$Type");
const $KeyMappingRegistry = Java.loadClass("dev.architectury.registry.client.keymappings.KeyMappingRegistry");

global.meleeSpecKey = new $KeyMapping(
    "key.kjs.melee",
    $KeConflictContext.IN_GAME,
    $KeyModifier.NONE,
    $InputConstantsType.MOUSE,
    0,
    "key.category.tacz",
);

StartupEvents.init(() => {
    $KeyMappingRegistry.register(global.meleeSpecKey);
});
