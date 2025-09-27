const $BlockPos = Java.loadClass('net.minecraft.core.BlockPos')

let side = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]

MaidRegister.TASK.walkToBlockTask("kubejs:crystal", "ae2:certus_quartz_crystal")
    .addConditionDesc("need_pickaxe", maid => maid.mainHandItem.hasTag("c:tools/mining_tool"))
    .setCloseEnoughDist(3)
    .setVerticalSearchRange(3) // 搜索范围,默认是2,太大影响性能
    .setSearchCondition(maid => {
        return maid.mainHandItem.hasTag("c:tools/mining_tool")
    })
    .setBlockPredicate( // 其实可以直接找水晶簇然后采的,但貌似女仆看不到太高的方块
        (maid, blockPos) => {
            return maid.level.getBlock(blockPos.getX(), blockPos.getY(), blockPos.getZ()).hasTag("c:budding_blocks")
        })
    .setArriveAction(
        (maid, blockPos) => {
            let level = maid.level
            side.forEach(value => {
                let x = blockPos.getX() + value[0]
                let y = blockPos.getY() + value[1]
                let z = blockPos.getZ() + value[2]
                let targetPos = $BlockPos(x, y, z)
                if (level.getBlock(x, y, z).hasTag("c:clusters")) {
                    maid.swing()
                    maid.destroyBlock(targetPos)
                    // 这边可以 maid.mainHandItem 获取主手镐子然后扣耐久,但是我认为没必要(
                }
            })
        })