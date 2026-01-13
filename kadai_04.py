from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('kadai #4  remove the columns')

x = 5
z = 10
for _n in range(7):
    y = param.Y_SEA + 1
    for _i in range(10):
        mc.setBlock(x, y, z,  param.IRON_BLOCK)
        sleep(0.1)
        y += 1
    x += 2

x = 5
z = 10
for _n in range(7):
    y = param.Y_SEA + 1
    for _i in range(10):
        mc.setBlock(x, y, z,  param.GOLD_BLOCK)
        sleep(0.1)
        y += 1
    x += 2

x = 5
z = 10
for _n in range(7):
    y = param.Y_SEA + 1
    for _i in range(10):
        mc.setBlock(x, y, z,  param.DIAMOND_BLOCK)
        sleep(0.1)
        y += 1
    x += 2

x = 5
z = 10
for _n in range(7):
    y = param.Y_SEA + 1
    for _i in range(10):
        mc.setBlock(x, y, z,  param.AIR)
        sleep(0.1)
        y += 1
    x += 2
