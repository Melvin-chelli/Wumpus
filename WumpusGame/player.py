import pygame

from .action import Action, table_of_actions
from random import choice


class Player(object):
    def __init__(self, size: int, ):
        self.score = 0
        self.coordinate = (0, 0)
        self.arrow = True
        self.gold = False
        self.breeze = False
        self.stench = False
        self.glitter = False
        self.size = size
        self.initParams()

    def initParams(self,):
        self.arrow = True
        self.got_gold = False
        self.wumpus_died = False
        self.agent_died = False
        self.escaped = False
        self.fadigue = 0
        self.hits = 0
        self.errors = 0
        self.escaped = False


    def act(self) -> Action:
        state = {
            'size': self.size,
            'coordinate': self.coordinate,
            'arrow': self.arrow,
        }
        action = getUserInput()

        return action

    def move(self, direction: str):
        x, y = self.coordinate

        if direction == 'U':
            self.coordinate = (x + 1, y)
        elif direction == 'D':
            self.coordinate = (x - 1, y)
        elif direction == 'R':
            self.coordinate = (x, y + 1)
        elif direction == 'L':
            self.coordinate = (x, y - 1)
        #print(self.coordinate)

    def shoot(self, ):
        self.arrow = False

    def pickUp(self, ):
        self.got_gold = True

    def hasPerception(self, perceptions):
        #(perceptions)
        if 'breeze' in perceptions:
            self.breeze = True
        else:
            self.breeze = False
        if 'stench' in perceptions:
            self.stench = True
        else:
            self.stench = False
        if 'glitter' in perceptions:
            self.glitter = True
        else:
            self.glitter = False


    def hasGold(self, ) -> bool:
        return self.got_gold

    def feelBreeze(self, )-> bool:
        return self.breeze

    def feelStench(self, )-> bool:
        return self.stench

    def feelGlitter(self, )-> bool:
        return self.glitter

    def hasArrow(self, ) -> bool:
        return self.arrow

    def die(self, ):
        self.agent_died = True

    def escape(self, ):
        self.escaped = True

    def reset(self, ):
        self.initParams()

    def killedWumpus(self, ) -> bool:
        return self.wumpus_died

    def wonGame(self, ) -> bool:
        return self.escaped

    def killWumpus(self, ):
        self.wumpus_died = True

def getUserInput():
    while 1:
        pressState = pygame.key.get_pressed()
        keyState = ''
        if pressState[pygame.K_UP]:
            # print("Up")
            keyState = table_of_actions['KU']
        if pressState[pygame.K_DOWN]:
            # print("Down")
            keyState =table_of_actions['KD']
        if pressState[pygame.K_LEFT]:
            # print("Left")
            keyState = table_of_actions['KL']
        if pressState[pygame.K_RIGHT]:
            # print("Right")
            keyState = table_of_actions['KR']
        if pressState[pygame.K_p]:
            # print("Pickup")
            keyState = table_of_actions['P']
        if pressState[pygame.K_w]:
            # print("Shoot Up")
            keyState = table_of_actions['SU']
        if pressState[pygame.K_s]:
            # print("Shoot Down")
            keyState = table_of_actions['SD']
        if pressState[pygame.K_d]:
            # print("Shoot Right")
            keyState = table_of_actions['SR']
        if pressState[pygame.K_a]:
            # print("Shoot Left")
            keyState = table_of_actions['SL']
        return keyState




