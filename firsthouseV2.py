# Joe Deller 2014
# This time our house has a pyramid roof and a rainbow over it

# Level : Intermediate
# Uses  : Libraries, variables, operators, loops, lists

# When designing a building, some squared paper can help with working out
# where to place things like doors and furniture

import mcpi.minecraft as minecraft
import mcpi.block as block
import math


def drawtree(x, y, z, tree_height, leaf_width):
    # Draw a simple tree, with a certain width of leaves
    # The bottom two layers
    leaves = leaf_width / 2
    mc.setBlocks(
        x - leaves - 1,
        y + tree_height + 1,
        z - leaves - 1,
        x + leaves + 1,
        y + tree_height + 2,
        z + leaves + 1,
        block.LEAVES.id)

    mc.setBlocks(
        x - 1,
        y + tree_height + 3,
        z,
        x + 1,
        y + tree_height + 4,
        z,
        block.LEAVES.id)

    mc.setBlocks(
        x,
        y + tree_height + 3,
        z - 1,
        x,
        y + tree_height + 4,
        z + 1,
        block.LEAVES.id)
    # Draw the trunk last, from the ground up
    mc.setBlocks(x, y - 1, z, x, y + tree_height + 2, z, block.WOOD.id)


def DrawHouse(x, y, z, house_width, house_height):
    # Draw a simple house at the coordinates given
    # draw the front of our house , with windows and torches
    # Our house is going to be 10 blocks deep and 8 blocks wide
    depth = 10
    middle = house_width / 2

    # Build a solid shape of stone
    # We could build a floor, walls and a roof, but starting with a solid block
    # then hollowing it out is less typing
    mc.setBlocks(
        x,
        y,
        z,
        x + house_width,
        y + house_height,
        z + depth,
        block.STONE.id)
    # Now hollow out the inside
    mc.setBlocks(
        x + 1,
        y + 1,
        z + 1,
        x + house_width - 1,
        y + house_height - 1,
        z + depth - 1,
        block.AIR.id)
    # Add windows
    mc.setBlocks(
        x + middle - 2,
        y + 2,
        z,
        x + middle + 2,
        y + 3,
        z,
        block.GLASS.id)

    # Now a front door
    # A door is made up of two blocks
    # The first is a solid panel
    # The second is a panel with glass in it
    mc.setBlock(x + middle, y + 1, z, block.DOOR_WOOD.id, 0)
    mc.setBlock(x + middle, y + 2, z, block.DOOR_WOOD.id, 8)

    # Let's have some torches for light, 2 blocks up
    # Torches on the right wall face east
    # Torches on the left wall face west
    # Right wall, four blocks back from front wall
    mc.setBlock(x + house_width - 1, y + 2, z + 4, block.TORCH.id, 2)
    # Left wall, four blocks back from front wall
    mc.setBlock(x + 1, y + 2, z + 4, block.TORCH.id, 1)

    # Two more near the back of the house
    # They need to be facing inwards

    # Right wall, nine blocks back from front wall
    mc.setBlock(x + house_width - 1, y + 2, z + 9, block.TORCH.id, 2)
    # left wall, nine blocks back from front wall
    mc.setBlock(x + 1, y + 2, z + 9, block.TORCH.id, 1)

    # draw some beds towards the back of the house
    # Like a door, a bed is made from two blocks
    # The blanket part and the pillow part
    # Beds can face in different directions
    # So you might need to experiment with which
    # parts go where
    mc.setBlock(x + 1, y + 1, z + 6, block.BED.id)
    mc.setBlock(x + 1, y + 1, z + 7, block.BED.id, 8)

    mc.setBlock(x + house_width - 1, y + 1, z + 6, block.BED.id)
    mc.setBlock(x + house_width - 1, y + 1, z + 7, block.BED.id, 8)

    # Now for some bookshelves at the back of the house
    # These will be two blocks high
    mc.setBlocks(
        x + middle - 1,
        y + 1,
        z + 9,
        x + middle + 1,
        y + 2,
        z + 9,
        block.BOOKSHELF.id)
    # Now for some lights in the walls at the back of our house
    # One block in from the edges of the walls

    mc.setBlock(x + 1, y + 2, z + depth, block.GLOWSTONE_BLOCK.id)
    mc.setBlock(
        x + house_width - 1,
        y + 2,
        z + depth,
        block.GLOWSTONE_BLOCK.id)


def Pyramid(x, y, z, width, depth, block_type):
    # build a pyramid shape out of the specified block_type
    # The width is used to decide how many layers there are
    # Rectangular shaped pyramids will be drawn if the width and depth are
    # different
    steps = x + int(width / 2) + 1
    for x1 in range(x, steps):
        mc.setBlocks(x, y, z, x + width, y, z + depth, block_type)
        y = y + 1
        z = z + 1
        x = x + 1
        depth = depth - 2
        width = width - 2


def grassland(x, y, z):
    mc.setBlocks(x - 34, y - 1, z - 24, x + 30, y - 1, z + 32, block.GRASS.id)
    mc.setBlocks(x - 40, y, z - 40, x + 40, y + 60, z + 40, block.AIR.id)

# Draw a rainbow, made from blocks of colored wool
# Experiment with the width and height to see the different shapes you get
# The rainbow will be one block deep

def rainbow(startX, playerY, playerZ, width, height):
    # Make a list of colours for our rainbow
    # Red = 14
    # Orange = 1
    # Yellow = 4
    # Green = 5 for lime green, 13 for dark green
    # Blue = 3 for light blue, 11 for dark blue
    # Indigo doesn't have a direct match, so we will use dark blue = 11
    # Violet = 10

    colors = [14, 1, 4, 5, 3, 11, 10]
    numColors = len(colors)

    for x in range(0, width):
        # for every colour we will draw one strand of the rainbow
        # stacked on top of each other
        for colour in range(0, numColors):
            y = math.sin((x / float(width)) * math.pi) * height + colour
            y = y + playerY
            mc.setBlock(startX + x - (width / 2),
                        int(y),
                        playerZ,
                        block.WOOL.id,
                        colors[len(colors) - 1 - colour])

# START HERE...
mc = minecraft.Minecraft.create()

# Get and store the player position
playerPos = mc.player.getTilePos()

player_x = playerPos.x
player_y = playerPos.y
player_z = playerPos.z

# First draw some grass where the player is standing
grassland(player_x, player_y, player_z)
# The trees will be 6 blocks back from where the player is standing
# One tree will be at the same X coordinate as the player
# The other will be 8 blocks to the right

# Our trees will have two blocks of leaves each side of the trunk
# They will be 3 blocks high

tree_z = player_z - 6
tree_height = 3
leaf_blocks = 2

drawtree(player_x + 8, player_y, tree_z, tree_height, leaf_blocks)
drawtree(player_x, player_y, tree_z, tree_height, leaf_blocks)
# The house will be 8 blocks back from where we are standing
# The floor needs to be one block lower than our feet

height = 4
width = 8
house_z = player_z + 8
DrawHouse(player_x, player_y - 1, house_z, width, height)
Pyramid(player_x, player_y + height, house_z, width, 10, block.WOOD_PLANKS.id)

# Some Torches for the outside of the house
mc.setBlock(player_x + 2, player_y + 3, player_z + 7, block.TORCH.id, 4)
mc.setBlock(player_x + 6, player_y + 3, player_z + 7, block.TORCH.id, 4)
mc.setBlock(player_x + 8, player_y + 3, player_z + 7, block.TORCH.id, 4)
mc.setBlock(player_x, player_y + 3, player_z + 7, block.TORCH.id, 4)
# Now draw a fairly big rainbow, a little bit back from the end
# of our houses

height = 28
width = 48

rainbow(player_x, player_y - 1, player_z + 10, width, height)
