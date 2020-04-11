import pygame as pg

import keyboardFunction

print('Keyboard library imported')

class Keyboard:
    def __init__(self,application):

        self.application = application

        self.status = [0,0]
        self.printStatus = True

    def handleEvent(self,pgEvent):
        if pgEvent.type==pg.KEYDOWN :
            if pgEvent.key==pg.K_LEFT :
                self.status[0] = -1
                self.keyboardPrint(keyboardFunction.KeyState.LEFT_ARROW_DOWN)
            elif pgEvent.key==pg.K_RIGHT :
                self.status[0] = 1
                self.keyboardPrint(keyboardFunction.KeyState.RIGHT_ARROW_DOWN)
        if pgEvent.type==pg.KEYDOWN :
            if pgEvent.key==pg.K_UP :
                self.status[1] = -1
                self.keyboardPrint(keyboardFunction.KeyState.UP_ARROW_DOWN)
            elif pgEvent.key==pg.K_DOWN :
                self.status[1] = 1
                self.keyboardPrint(keyboardFunction.KeyState.DOWN_ARROW_DOWN)
        if pgEvent.type==pg.KEYUP  :
            if pg.key.get_pressed()[pg.K_LEFT] and not pg.key.get_pressed()[pg.K_RIGHT] :
                self.status[0] = -1
                self.keyboardPrint(keyboardFunction.KeyState.LEFT_ARROW_DOWN)
            elif pg.key.get_pressed()[pg.K_RIGHT] and not pg.key.get_pressed()[pg.K_LEFT] :
                self.status[0] = 1
                self.keyboardPrint(keyboardFunction.KeyState.RIGHT_ARROW_DOWN)
            elif not pg.key.get_pressed()[pg.K_LEFT] and not pg.key.get_pressed()[pg.K_RIGHT] :
                self.status[0] = 0
        if pgEvent.type==pg.KEYUP  :
            if pg.key.get_pressed()[pg.K_UP] and not pg.key.get_pressed()[pg.K_DOWN] :
                self.status[1] = -1
                self.keyboardPrint(keyboardFunction.KeyState.UP_ARROW_DOWN)
            elif pg.key.get_pressed()[pg.K_DOWN] and not pg.key.get_pressed()[pg.K_UP] :
                self.status[1] = 1
                self.keyboardPrint(keyboardFunction.KeyState.DOWN_ARROW_DOWN)
            elif not pg.key.get_pressed()[pg.K_UP] and not pg.key.get_pressed()[pg.K_DOWN] :
                self.status[1] = 0

    def keyboardPrint(self,keyState):
        if self.printStatus :
            print(keyState)



    # def handleEvent(self,pgEvent):
    #     if self.keyboard.arrows[1]==-1 :
    #         gl.playSound(upSound)
    #     if self.keyboard.arrows[1]==1 :
    #         gl.playSound(downSound)
    #     if self.keyboard.arrows[0]==1 :
    #         gl.playMusic('Sounds/TakeaWalk.mp3')
    #     if self.keyboard.arrows[0]==-1 :
    #         gl.playSound(leftSound)
