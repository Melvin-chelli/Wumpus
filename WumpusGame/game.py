from time import sleep

from . import Action
from .gui.screen import Screen
from .player import Player
class Game(object):
    def __init__(self, environment, gui_enabled, agent = None):
        self.environment = environment
        self.agent = Player(1)
        self.game_over = False
        self.screen = Screen()
        self.gui_enabled = gui_enabled


    def start(self) -> None:
        if self.gui_enabled:
            self.screen.show(self.environment.dimension)
            self.screen.addAgents(self.agent)
            self.screen.addWumpus(self.environment.getObjectCoord("wumpus"))
            self.screen.addPits(self.environment.getObjectCoord("pit"))
            self.screen.addGold(self.environment.getObjectCoord("gold"))
        
        while not self.agent.agent_died and not self.agent.escaped:
            if self.gui_enabled: self.screen.updateComponents()
            agent_action = self.agent.act()

            if isinstance(agent_action, Action):
                if agent_action.name == 'move':
                    # self.screen.moveAgent(agent, agent_action.direction)
                    self.agent.move(agent_action.direction)
                    coordinate = self.agent.coordinate
                    if self.environment.isValid(coordinate):
                        self.agent.hits += 1
                    else:
                        self.agent.errors += 1
                    if self.environment.isPit(coordinate):
                        # self.screen.killAgent(agent)
                        self.agent.die()
                        print('agent died')
                        continue

                    if self.environment.isWumpus(coordinate) and not self.agent.killedWumpus():
                        # self.screen.killAgent(agent)
                        self.agent.die()
                        print('agent died')
                        continue

                    if self.environment.isExit(coordinate) and self.agent.hasGold():
                        self.agent.escape()
                        print('agent wins')
                        continue
                    # self.screen.updatePerceptions(self.agent)
                    perceptions = self.environment.getPerceptions(coordinate)
                    self.agent.hasPerception(perceptions)


                if agent_action.name == 'shoot':
                    if not self.agent.hasArrow():
                        # agent.errors += 0.1
                        continue
                    self.agent.shoot()
                    targetCoordinate = self.targetCoordinate(self.agent.coordinate, agent_action.direction)
                    print('agent took a shot: ' + agent_action.direction)
                    if self.environment.isWumpus(targetCoordinate) and not self.agent.killedWumpus():
                        self.agent.killWumpus()
                        self.agent.hits += 1
                        print('agent killed wumpus')
                if agent_action.name == 'pickup':
                    if not self.agent.hasGold() and self.environment.isGold(self.agent.coordinate):
                        self.agent.pickUp()
                        self.agent.hits += 1
                    else:
                        # agent.errors += 0.1
                        pass

                            # print('agent took gold')
                sleep(0.3)
        sleep(2)
        print("Game Over")



    def targetCoordinate(self, coordinate:tuple, direction:str) -> tuple:
        x,y = coordinate
        if   direction == 'U': return (x+1,y)
        elif direction == 'D': return (x-1,y)
        elif direction == 'R': return (x,y+1)
        elif direction == 'L': return (x,y-1)
    

        
