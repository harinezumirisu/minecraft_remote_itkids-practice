from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('kadai #9  house')

mc.setBlocks(71, param.Y_SEA + 1, 48,   48, param.AXIS_TOP,    71,    param.AIR)

def setPyramid(mc=mc, x=0, z=0, size=3, y=param.Y_SEA + 1, blockTypeId=param.GOLD_BLOCK):
    while size > 0:
        mc.setBlocks(x, y, z, x + size - 1, y, z + size - 1, blockTypeId)
        x += 1
        z += 1
        size -= 2
        y += 1
        sleep(0.01)

if __name__ == "__main__":
    setPyramid(x=48, z=48, y=param.Y_SEA + 9, size=23, blockTypeId=param.SHROOMLIGHT)
    setPyramid(x=49, z=49, y=param.Y_SEA + 9, size=21, blockTypeId=param.AIR)

mc.setBlocks(49, param.Y_SEA + 1, 49,   69, param.Y_SEA+9,    69,    param.IRON_BLOCK)
mc.setBlocks(50, param.Y_SEA + 2, 50,   68, param.Y_SEA+9,    68,    param.AIR)
