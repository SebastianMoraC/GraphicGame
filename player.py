import pygame, sys
from pygame.draw import rect
from pygame.locals import *

WIDTH = 800
HEIGHT = 800

class Xena(pygame.sprite.Sprite):
    def __init__(self, position,speed):
        self.speed = speed
        self.player = pygame.image.load('images/xena.png')
        self.player.set_clip(pygame.Rect(0,0,52,76)) #Look in the paint the direction to rect the image in the sprite - This is to select the clip
        self.clipping = self.player.subsurface(self.player.get_clip())
        self.rectClip = self.clipping.get_rect()
        self.rectClip.topleft = position
        self.figure = 0
        self.statesLeft = {0: (0,76,52,76), 1: (52,76,52,76), 2: (156,76,52,76)}
        self.statesRight = {0: (0,152,52,76), 1: (52,152,52,76), 2: (156,152,52,76)} #Coords (x,y,width,heigth)
        self.statesUp = {0: (0,228,52,76), 1: (52,228,52,76), 2: (156,228,52,76)}
        self.statesDown = {0: (0,0,52,76), 1: (52,0,52,76), 2: (156,0,52,76) }

    def get_figure(self, states):
        self.figure += 1
        if self.figure >= (len(states)):
            self.figure = 0
        return states[self.figure]
    
    def cut(self, rectClipping):
        if type(rectClipping) is dict:
            self.player.set_clip(pygame.Rect(self.get_figure(rectClipping)))
        else:
            self.player.set_clip(pygame.Rect(rectClipping))
        return rectClipping 

    def updateSprite(self, direction):
        if direction == "left":
            self.cut(self.statesLeft)
            self.rectClip.x -= self.speed 
            if self.rectClip.left < 0:
                self.rectClip.left = 0
        elif direction == "right":
            self.cut(self.statesRight)
            self.rectClip.x += self.speed 
            if self.rectClip.right > WIDTH:
                self.rectClip.right = WIDTH
        elif direction == "up":
            self.cut(self.statesUp)
            self.rectClip.y -= self.speed 
            if self.rectClip.top < 0:
                self.rectClip.top = 0
        elif direction == "down":
            self.cut(self.statesDown)
            self.rectClip.y += self.speed 
            if self.rectClip.bottom > HEIGHT:
                self.rectClip.bottom = HEIGHT
        
        elif direction == "stopLeft":
            self.cut(self.statesLeft[0])
        elif direction == "stopRight":
            self.cut(self.statesRight[0])
        elif direction == "stopUp":
            self.cut(self.statesUp[0])
        elif direction == "stopDown":
            self.cut(self.statesDown[0])
        
        self.clipping = self.player.subsurface(self.player.get_clip())

    def eventS(self, event):
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.updateSprite("left")
            elif event.key == K_RIGHT:
                self.updateSprite("right")
            elif event.key == K_DOWN:
                self.updateSprite("down")
            elif event.key == K_UP:
                self.updateSprite("up")

        elif event.type == KEYUP: #Dont Push
            if event.key == K_LEFT:
                self.updateSprite("stopLeft")
            elif event.key == K_RIGHT:
                self.updateSprite("stopRight")
            elif event.key == K_DOWN:
                self.updateSprite("stopDown")
            elif event.key == K_UP:
                self.updateSprite("stopUp")
    