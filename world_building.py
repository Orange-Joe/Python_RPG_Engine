from dialog import *
import os
import sys
import readchar
import pygame
import time


__author__ = "0range-j0e"
__copyright__ = "0range-j0e"
__version__ =  "1.0"

"""
This module is a major work in progress for an interactice map based on Unicode characters. Currently working on refactoring this code to improve
the ease in which new maps can be created and interacted with by creating a standard grid strucutre. Running this program will put the player in 
a test map in which the player can move around and add new objects to the world by using the build function. Please see the building function below 
for more information. Please note you will likely need to zoom into the terminal to see the map properly.   
"""


inv = []
last_door = None
game_over = False

# List of map objects starting with the player icon. 
p = (green + dim + 'π')
# Wizard icon
z = (green + dim + 'W')
# Wall
w = (normal + "|")
# First map door
d = (red+bright+"D")
# Second map door
d1 = black + bright + "D"
# Second map return door
d2 = white + dim + "D"
q = white + bright + "X"
w1 = black + bright + "|"
c1 = black + bright + "-"
k = [blue + 'K', 'BLUE KEY']

# Village Square Map
map  =  [w,'X', 'O', 'X','X','X','X','X','X','X', w,
        w,'X','X','X','X','X','X','X','X','X',w,
        w,'X','X','X','X','X','X','X','X','X',w, 
        w,'X','X','X','X','X','X','X','X','X',w, 
        w,'X','X','X','X','X', z, 'X', d,'X',  w]


previous_map = None
# WIP maps
map1 = [' ', ' ', ' ', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', ' ', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', ' ', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', '\x1b[34m\x1b[2m_', ' ', ' ', '\x1b[34m|', '\x1b[34m\x1b[2m⍿', '\x1b[34m\x1b[1m⏣', '\x1b[34m\x1b[2m⍿', '\x1b[33m\x1b[1m\x1b[34m\x1b[1m∞', '\x1b[34m\x1b[2m⍿', '\x1b[34m\x1b[1m⏣', '\x1b[34m\x1b[2m⍿', '\x1b[34m|', '\x1b[30m\x1b[1m⚱', '\x1b[30m\x1b[1m⚱', '\x1b[33m\x1b[1m⚚', '\x1b[34m|', '\x1b[31m\x1b[1m♨', '\x1b[31m\x1b[1m♨', '\x1b[34m|', '\x1b[33m\x1b[1m☤', '\x1b[30m\x1b[1m⚱', '\x1b[30m\x1b[1m⚱', '\x1b[34m\x1b[2m╠', '\x1b[34m\x1b[2m╬', '\x1b[34m\x1b[2m╬', '\x1b[34m\x1b[34m\x1b[1m⏣', '\x1b[34m\x1b[34m\x1b[1m⏣', '\x1b[34m\x1b[2m╬', '\x1b[34m\x1b[2m╬', '\x1b[34m\x1b[2m╣', ' ', ' ', '\x1b[34m|', '\x1b[34m\x1b[2m⍿', '\x1b[32m\x1b[2m⬖', '\x1b[34m\x1b[2m⍿', '\x1b[31m\x1b[2m⌔', '\x1b[34m\x1b[2m⍿', '\x1b[32m\x1b[2m⬗', '\x1b[34m\x1b[2m⍿', '\x1b[34m|', ' ', ' ', ' ', ' ', '\x1b[31m\x1b[2m‾', '\x1b[31m\x1b[2m‾', ' ', ' ', ' ', ' ', '\x1b[34m╠', '\x1b[34m╬', '\x1b[34m╬', '\x1b[34m╬', '\x1b[34m╬', '\x1b[34m╬', '\x1b[34m╬', '\x1b[34m╣', ' ', ' ', '\x1b[34m|', '\x1b[34m\x1b[2m⍿', ' ', ' ', ' ', ' ', ' ', ' ', '\x1b[34m|', ' ', ' ', '\x1b[32m☘', '\x1b[32m\x1b[2m☘', '\x1b[31m\x1b[2m☘', '\x1b[34m☘', '\x1b[32m☘', '\x1b[32m\x1b[2m☘', ' ', ' ', '\x1b[34m\x1b[2m╚', '\x1b[34m\x1b[2m╩', '\x1b[34m\x1b[2m╬', '\x1b[34m\x1b[2m╬', '\x1b[34m\x1b[2m╬', '\x1b[34m\x1b[2m╬', '\x1b[34m\x1b[2m╩', '\x1b[34m\x1b[2m╣', ' ', ' ', '\x1b[34m|', '\x1b[34m\x1b[1m▩', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\x1b[32m☘', '\x1b[32m\x1b[2m☘', '\x1b[34m☘', '\x1b[34m\x1b[2m☘', '\x1b[31m\x1b[2m☘', '\x1b[35m\x1b[2m☘', '\x1b[32m\x1b[2m☘', '\x1b[32m☘', ' ', ' ', ' ', '\x1b[34m\x1b[2m╚', '\x1b[34m\x1b[1m▩', '\x1b[34m\x1b[1m▩', '\x1b[34m\x1b[2m╝', ' ', '\x1b[34m\x1b[2m║', ' ', ' ', '\x1b[34m|', '\x1b[34m\x1b[1m▩', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\x1b[31m☘', '\x1b[32m☘', '\x1b[31m\x1b[2m☘', '\x1b[33m\x1b[2m☘', '\x1b[35m\x1b[2m☘', '\x1b[31m☘', '\x1b[32m\x1b[2m☘', '\x1b[31m\x1b[2m☘', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\x1b[34m\x1b[2m║', ' ', ' ', '\x1b[34m|', '\x1b[34m\x1b[2m⍿', ' ', ' ', ' ', ' ', ' ', ' ', '\x1b[34m|', ' ', ' ', '\x1b[33m\x1b[2m☘', '\x1b[32m☘', '\x1b[32m\x1b[2m☘', '\x1b[34m\x1b[2m☘', '\x1b[32m\x1b[2m☘', '\x1b[32m☘', ' ', ' ', '\x1b[34m\x1b[2m╔', '\x1b[34m\x1b[2m╦', '\x1b[34m\x1b[2m╦', '\x1b[34m▩', '\x1b[34m▩', '\x1b[34m\x1b[2m╦', '\x1b[34m\x1b[2m╦', '\x1b[34m\x1b[2m╣', ' ', ' ', '\x1b[34m|', '\x1b[34m\x1b[2m⍿', '\x1b[32m\x1b[2m⬖', '\x1b[34m\x1b[2m⍿', '\x1b[31m\x1b[2m▵', '\x1b[34m\x1b[2m⍿', '\x1b[32m\x1b[2m⬗', '\x1b[34m\x1b[2m⍿', '\x1b[34m|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\x1b[34m\x1b[2m╠', '\x1b[34m\x1b[2m╬', '\x1b[34m\x1b[2m╬', '\x1b[34m\x1b[2m╬', '\x1b[34m\x1b[2m╬', '\x1b[34m\x1b[2m╬', '\x1b[34m\x1b[2m╬', '\x1b[34m\x1b[2m╣', ' ', ' ', '\x1b[34m|', '\x1b[34m\x1b[2m⍿', '\x1b[34m\x1b[1m⏣', '\x1b[34m\x1b[2m⍿', '\x1b[33m\x1b[1m\x1b[34m\x1b[1m∞', '\x1b[34m\x1b[2m⍿', '\x1b[34m\x1b[1m⏣', '\x1b[34m\x1b[2m⍿', '\x1b[34m|', ' ', '\x1b[30m\x1b[1m⚰', '\x1b[30m\x1b[1m⚰', '\x1b[30m\x1b[1m⚰', '\x1b[30m\x1b[1m⚰', '\x1b[30m\x1b[1m⚰', '\x1b[30m\x1b[1m⚰', '\x1b[30m\x1b[1m⚰', '\x1b[30m\x1b[1m⚰', ' ', '\x1b[34m╠', '\x1b[34m╬', '\x1b[34m╬', '\x1b[34m\x1b[34m\x1b[1m⏣', '\x1b[34m\x1b[34m\x1b[1m⏣', '\x1b[34m╬', '\x1b[34m╬', '\x1b[34m╣', ' ', ' ', ' ', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', ' ', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', ' ', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m\x1b[34m\x1b[2m⎺', '\x1b[34m\x1b[2m⎺']


#Open World Map
map2 = ['┌', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '┐', ' ', ' ', ' ', '◬', ' ', ' ', '◬', ' ', ' ', ' ', '\x1b[22m|', '\x1b[37m\x1b[2mD', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '*', '\\', '/', '*', '\\', ' ', ' ', '\x1b[22m|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '☠', ' ', ' ', ' ', ' ', ' ', '-', '-', '/', '/', ' ', '\\', '/', ' ', '\\', '\\', ' ', '\x1b[22m|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '⚕', ' ', ' ', ' ', ' ', ' ', '└', '/', '/', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '\\', '\x1b[22m|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ⚱', ' ', ' ', ' ', '/', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '☺', ' ', ' ', ' ', '/', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' |', '├', '\x1b[30m\x1b[1m-', '\x1b[30m\x1b[1m-', '\x1b[30m\x1b[1m-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' /', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', blue +  '|', blue +  '|', '\x1b[22m|', ' ', ' ', ' ', ' ', '\x1b[30m\x1b[1m|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' |', blue +  '|', '\x1b[22m|', ' ', ' ', ' ', ' ', '\x1b[30m\x1b[1m|', '\x1b[32m\x1b[2mW', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' |', blue +  '|', '└', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ' ']

# WIP maps
# map3 = [' ', ' ', ' ', blue + dim + '_', blue + dim + '_', blue + dim + '_', '⍙', blue + dim + '_', blue + dim + '_', blue + dim + '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', blue +  '|', blue + dim + '⍿', blue + bright + '⏣', blue + dim + '⍿', yellow + bright + blue + bright  + '∞', blue + dim + '⍿', blue + bright + '⏣', blue + dim + '⍿', blue +  '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', blue +  '|', blue + dim + '⍿', green  + dim + '⬖', blue + dim + '⍿', red + dim  + '⌔', blue + dim + '⍿', green  + dim + '⬗', blue + dim + '⍿', blue +  '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', blue +  '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', blue +  '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', blue +  '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', blue +  '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', blue +  '|', yellow + bright + '☤', ' ', ' ', ' ', '♾', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', blue +  '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', blue +  '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', blue +  '|', blue + dim + '⍿', green  + dim + '⬖', blue + dim + '⍿', red + dim  + '▵', blue + dim + '⍿', green  + dim + '⬗', blue + dim + '⍿', blue +  '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', blue +  '|', blue + dim + '⍿', blue + bright + '⏣', blue + dim + '⍿', yellow + bright + blue + bright  + '∞', blue + dim + '⍿', blue + bright + '⏣', blue + dim + '⍿', blue +  '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', blue + dim + blue  + dim + '⎺', blue + dim + blue  + dim + '⎺', blue + dim + blue  + dim + '⎺', blue + dim + blue  + dim + '⎺', blue + dim + blue  + dim + '⎺', blue + dim + blue  + dim + '⎺', blue + dim + blue  + dim + '⎺', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
map3 =['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']


location = 'Village Square' 


"""
The build function allows the player to add their own Unicode characters to a map. To call the function, press 'b'.
Once you've pressed 'b', you can choose to add an object above, below, left, or right. Example: press 'b' > type: 'w ⌨' (no quotes and there
must be a space between 'b' and '⌨'. This will add a keyboard object above the player. This is a work in progress, but can theoretically be 
used to create fully fleshed-out Unicode maps. To add colors to the Unicode character you're adding, type color + character, ex:
'w blue + ⌨'. In the future I want the build function to identify custom Python objects and add them into the game intellgiently, such as doors
that lead to a certain location or a sword with special properties. If you want to save a map you have modified, exit into the interpreter, print
the map object, and copy and paste it into the code.    
"""
def build(map, w, a, s, d):

    print("w = build above\nd = build to right\ns = build below\na = build to left")
    x = input(":: ")
    indices = []
    # a = x
    if len(x) > 2:
        if ' ' in x:
            # go = input('space found in command')
            while ' ' in x:
                x = list(x)
                x.remove(' ')
                x = ''.join(x)
    
    if x[-1] == ' ':
        x = list(x)
        x.append(' ')
        x = ''.join(x)

    while '+' in x:
        check = x.find('+')
        print(check)
        if check != -1:
            indices.append(check)
            print(indices)
            x_list = list(x.strip(''))
            x_list.pop(check)
            x = ''.join(x_list)


    if x[:1].lower() == 'w':
        if len(x) < 3:
            map[w] = x[1:]

        
        if len(indices) == 1:
            try:
                map[w] = (Dialog.colors[x[1:(indices[0])]] + x[-1])
            except:
                pass
        elif len(indices) == 2:
            try:
                map[w] = ((Dialog.colors[x[1:(indices[0])]]) + (Dialog.colors[x[(indices[0]):(indices[1])]]) +  x[-1])
            except:
                pass

    elif x[:1].lower() == 'a':
        if len(x) < 3:
            map[a] = x[1:]

        
        if len(indices) == 1:
            try:
                map[a] = (Dialog.colors[x[1:(indices[0])]] + x[-1])
            except:
                pass
        elif len(indices) == 2:
            try:
                map[a] = ((Dialog.colors[x[1:(indices[0])]]) + (Dialog.colors[x[(indices[0]):(indices[1])]]) +  x[-1])
            except:
                pass


    elif x[:1].lower() == 's':
        if len(x) < 3:
            map[s] = x[1:]

        
        if len(indices) == 1:
            try:
                map[s] = (Dialog.colors[x[1:(indices[0])]] + x[-1])
            except:
                pass
        elif len(indices) == 2:
            try:
                map[s] = ((Dialog.colors[x[1:(indices[0])]]) + (Dialog.colors[x[(indices[0]):(indices[1])]]) +  x[-1])
            except:
                pass


    elif x[:1].lower() == 'd':
        if len(x) < 3:
            map[d] = x[1:]

        
        if len(indices) == 1:
            try:
                map[d] = (Dialog.colors[x[1:(indices[0])]] + x[-1])
            except:
                pass
        elif len(indices) == 2:
            try:
                map[d] = ((Dialog.colors[x[1:(indices[0])]]) + (Dialog.colors[x[(indices[0]):(indices[1])]]) +  x[-1])
            except:
                pass


    elif x == 'u':
        map = previous_map    


def output(plots,check, end):
    cursor.hide()
    for i in range(check, end):

        # if plots[i] in ['╔','╚', '═']:
        #     if plots[i+1] != ' ':
        #         print(f"{plots[i]}", end="═", flush=True)
        
        # elif plots[i] in ['-']:
        #     if plots[i+1] != ' ':
        #         print(f"{plots[i]}", end="-", flush=True)

        if type(plots[i]) is list:
            a = plots[i][0]
            print(f"{a}", end="", flush=True)
        
        else:
            # print(f"{plots[i]}", end="", flush=True)
            # print(plots[i], end="", flush=True)
            sys.stdout.write(plots[i])
    cursor.show()
    print("")



def point_check(plots, point):

    if 'W' in plots[point]:
        return True
    else:
        return False

def door_check(plots, point):

    if 'D' in plots[point]:
        return True
    else:
        return False

def block_check(plots, point):

    block_points = ['╝', blue +  '|', '-', '╚', '╗', '╔' ]
    
    for i in block_points:
    
        if i in plots[point]:        
            return True
    return False


def village_square():

    def wiz_chat():
        Dialog.quick_chat("""\nWIZARD:\n\nWhy hello, Stranger! """, blue + dim)
    
        input("Continue... ")

    def checks(c, n, map, x):
        block = block_check(map,n)
        if block is False:
            door = door_check(map,n)
            if door is True:
                map[(x)] = c
                last_door = map[n]
                return ('door', c)
            elif door is False:
                chat = point_check(map,n)
                if chat is False:
                    map[(x)] = c
                    c = map[n]
                    x = n
                    first_round = False
                    return (x, c)
                elif chat is True:
                    wiz_chat()
                    return (x, c)
        elif block is True:
            return (x, c)
        else:
            c = map[n]
            return (x, c)
   
    # In Village Square, player starts off on map plot map[1].
    # If the player were returning from another location, there should be a bool to determine if that's the case
    # and put the player at the map plot point next to the door instead of the first spawn point. 
    x = 1
    # current plot point
    c = map[x]
    first_round = True

    chat = False
    block = False
    door = False 

    while True:

        map[x] = p
        os.system('clear')

        Dialog.quick_chat("\n-- Village  Square --", blue + dim)
        # print(f"LAST DOOR: {last_door}")
        output(map,0,11)
        output(map,11,22)
        output(map,22,33)
        output(map,33,44)
        output(map,44,55)

        if chat is False:

            inp = repr(readchar.readchar()) 

            try:

                if inp == "'w'":
                    n = x-11
                    x, c = checks(c, n, map, x)
                elif inp == "'a'":
                    n = x-1
                    x, c = checks(c, n, map, x)
                elif inp == "'s'":
                    n = x+11
                    x, c = checks(c, n, map, x)
                elif inp == "'d'":
                    n = x+1
                    x, c = checks(c, n, map, x)

                elif inp == "'c'":
                    a = input("Enter command: ")
                    if a == 'quit':
                        os.system('quit')
                        break

                elif inp == "'b'":
                    build(map, x-11, x-1, x+11, x+1)

                elif inp == "'q'":
                    sys.exit()

                else:
                    pass   

                if x == 'door':
                    break             
                block = False


            
            except:
                pass
        
        


def open_world():

    
    def wiz_chat():
        Dialog.quick_chat("""\nWIZARD:\n\nWhy hello, Stranger!""", blue + dim)
    
        input("Continue... ")

    def checks(c, n, map, x):
        block = block_check(map,n)
        if block is False:
            door = door_check(map,n)
            if door is True:
                map[(x)] = c
                last_door = map[n]
                return ('door', c)
            elif door is False:
                chat = point_check(map,n)
                if chat is False:
                    map[(x)] = c
                    c = map[n]
                    x = n
                    first_round = False
                    return (x, c)
                elif chat is True:
                    wiz_chat()
                    return (x, c)
        elif block is True:
            return (x, c)
        else:
            c = map[n]
            return (x, c)

    # In Village Square, player starts off on map plot map[1].
    # If the player were returning from another location, there should be a bool to determine if that's the case
    # and put the player at the map plot point next to the door instead of the first spawn point. 
    x = 32
    
    c = map1[x]
    first_round = True

    chat = False
    block = False
    door = False

    while True:

        map1[x] = p
        os.system('clear')

        output(map1,0,29)
        output(map1,29,58)
        output(map1,58,87)
        output(map1,87,116)
        output(map1,116,145)
        output(map1,145,174)
        output(map1,174,203)
        output(map1,203,232)
        output(map1,232,261)
        output(map1,261,290)

    
        if chat is False:

            inp = repr(readchar.readchar())
            
            try:

                if inp == "'w'":
                    n = x-29
                    x, c = checks(c, n, map1, x)

                elif inp == "'a'":
                    n = x-1
                    x, c = checks(c, n, map1, x)

                elif inp == "'s'":
                    n = x+29
                    x, c = checks(c, n, map1, x)

                elif inp == "'d'":
                    n = x+1
                    x, c = checks(c, n, map1, x)


                elif inp == "'c'":
                    a = input(": ")
                    if a == 'quit':
                        os.system('quit')
                        break
                    else:
                        try:
                            os.system(f'{a}')
                        except:
                            pass
            
                elif inp == "'b'":
                    build(map1, x-29, x-1, x+29, x+1)

                if x == 'door':
                    break  
                block = False
            
            except:
                pass


def grid():

    def wiz_chat():
        Dialog.quick_chat("""\nWIZARD:\n\nWhy hello, Stranger! """, blue + dim)
    
        input("Continue... ")

    def checks(c, n, map, x):
        block = block_check(map,n)
        if block is False:
            door = door_check(map,n)
            if door is True:
                map[(x)] = c
                last_door = map[n]
                return ('door', c)
            elif door is False:
                chat = point_check(map,n)
                if chat is False:
                    map[(x)] = c
                    c = map[n]
                    x = n
                    first_round = False
                    return (x, c)
                elif chat is True:
                    wiz_chat()
                    return (x, c)
        elif block is True:
            return (x, c)
        else:
            c = map[n]
            return (x, c)

    # In Village Square, player starts off on map plot map[1].
    # If the player were returning from another location, there should be a bool to determine if that's the case
    # and put the player at the map plot point next to the door instead of the first spawn point. 
    x = 500
    
    c = map3[x]
    first_round = True

    chat = False
    block = False
    door = False

    while True:

        map3[x] = p
        os.system('clear')

        output(map3,0,100)
        output(map3,100,200)
        output(map3,200,300)
        output(map3,300,400)
        output(map3,400,500)
        output(map3,500,600)
        output(map3,600,700)
        output(map3,700,800)
        output(map3,800,900)
        output(map3,900,1000)
        output(map3,1000,1100)
        output(map3,1100,1200)
        output(map3,1200,1300)
        output(map3,1300,1400)
        output(map3,1400,1500)
        output(map3,1500,1600)
        output(map3,1600,1700)
        output(map3,1700,1800)
        output(map3,1800,1900)
        output(map3,1900,2000)

    
        if chat is False:

            inp = repr(readchar.readchar())
            
            try:

                if inp == "'w'":
                    n = x-100
                    x, c = checks(c, n, map3, x)

                elif inp == "'a'":
                    n = x-1
                    x, c = checks(c, n, map3, x)

                elif inp == "'s'":
                    n = x+100
                    x, c = checks(c, n, map3, x)

                elif inp == "'d'":
                    n = x+1
                    x, c = checks(c, n, map3, x)


                elif inp == "'c'":
                    a = input(": ")
                    if a == 'quit':
                        os.system('quit')
                        break
                    else:
                        try:
                            os.system(f'{a}')
                        except:
                            pass
            
                elif inp == "'b'":
                    build(map3, x-100, x-1, x+100, x+1)

                if x == 'door':
                    break  
                block = False
            
            except:
                pass


open_world()
