
#Hello World
from mcpi.minecraft import *

mc = Minecraft.create()
mc.postToChat("Hello  World")



import mcpi.minecraft as Minecraft
from House_Complete import *

mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
house(x+10,y,z)

#Teleport
from mcpi.minecraft import *

mc = Minecraft.create()
mc.postToChat("Hello  World")

x,y,z = mc.player.getPos()
mc.player.setPos(x-5,y+50,z)

#Set Block
from mcpi.minecraft import *

mc = Minecraft.create()
mc.postToChat("Hello  World")

x,y,z = mc.player.getPos()
mc.setBlock(x+1,y,z,1)

#Creating a Column
from mcpi.minecraft import *

mc = Minecraft.create()
mc.postToChat("Hello  World")

x,y,z = mc.player.getPos()
mc.setBlock(x+3,y,z,1)
mc.setBlock(x+3,y+1,z,1)
mc.setBlock(x+3,y+2,z,1)

#Block Constants
from mcpi.minecraft import *
from mcpi import block

mc = Minecraft.create()
mc.postToChat("Hello  World")

x,y,z = mc.player.getPos()
mc.setBlock(x+3,y,z,block._BLOCK.id)

#Block as a variable
from mcpi.minecraft import *
from mcpi import block

mc = Minecraft.create()
mc.postToChat("Hello  World")

x,y,z = mc.player.getPos()
dirt=3
mc.setBlock(x+1,y,z,dirt)

#Special Blocks
from mcpi.minecraft import *
from mcpi import block

mc = Minecraft.create()
mc.postToChat("Hello  World")

x,y,z = mc.player.getPos()
wool=35
mc.setBlock(x+1,y,z,wool,1)

#Set Multiple Blocks
from mcpi.minecraft import *
from mcpi import block

mc = Minecraft.create()
mc.postToChat("Hello  World")

x,yz = mc.player.getPos()
stone=1
mc.setBlocks(x+1,y+1,z+1,x+11,y+11,z+11,stone)

#Fun with TNT
from mcpi.minecraft import *
from mcpi import block

mc = Minecraft.create()
mc.postToChat("Hello  World")

x,y,z = mc.player.getPos()
tnt=46
mc.setBlocks(x+1,y+1,z+1,x+11,y+11,z+11,tnt,1)

#Fun with Lava
from mcpi.minecraft import *
from mcpi import block

mc = Minecraft.create()

x,y,z = mc.player.getPos()
lava=10
mc.setBlock(x+3,y+3,z+3,lava)

#More Fun with Lava
from mcpi import block
from time import sleep

mc = Minecraft.create()

x,y,z = mc.player.getPos()

lava=10
water=8
air=0

mc.setBlock(x+3,y+3,z+3,lava)
sleep(3)
mc.setBlock(x+3,y+3,z+3,water)
sleep(5)
mc.setBlock(x+3,y+3,z+3,air)

#Make a house
from mcpi.minecraft import *
from House_Complete import *

mc = Minecraft.create()

x,y,z = mc.player.getPos()

house(x+10,y,z)


#Make 10 houses
from mcpi.minecraft import *
from House_Complete import *

mc = Minecraft.create()

x,y,z = mc.player.getPos()

for number in range(10,100,10):
    print(number)
    house(x+number,y,z)







