import pygame
import os
from WumpusGame import player
from WumpusGame.player import Player

WHITE = (200,200,200)
BACKGROUND = (155,155,155)

class Screen(object):
    def __init__(self,):
        self.WIDTH = None
        self.HEIGHT = None
        self.screen = None
        self.square_size = None
        self.square_x = None
        self.square_y = None
        self.initial_x = None
        self.initial_y = None
        self.part = None
        self.parts = None
        self.generation = 0
        self.score = 0
        self.img_wumpus = None
        self.img_pit = None
        self.img_gold = None
        self.img_agent = None
        self.img_status_agent = None
        self.img_stench = None
        self.img_breeze = None
        self.agents = []
        self.generation = None
        self.clock = pygame.time.Clock()
        self.fps = 240
        self.breeze_coord = []
        self.stench_coord = []
        self.glitter_coord = []

    def show(self, dimension):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))

        self.WIDTH = self.screen.get_width()
        self.HEIGHT = self.screen.get_height()
        self.initial_x, self.initial_y = self.WIDTH//3, self.HEIGHT//4
        self.square_size = self.HEIGHT//2
        self.square_x = self.initial_x + self.square_size
        self.square_y = self.initial_y + self.square_size
        self.parts = dimension
        self.part = self.square_size//self.parts
        self.loadComponets()


    def loadComponets(self,):
        self.img_wumpus = [
            pygame.image.load(os.path.abspath('img/monster.png')),
            pygame.image.load(os.path.abspath('img/monster.png'))
        ]

        self.img_wumpus = [pygame.transform.scale(img, (self.part-1,self.part-1)) for img in self.img_wumpus]
        self.img_wumpus[0] = pygame.transform.rotate(self.img_wumpus[0],-5)
        self.img_wumpus[1] = pygame.transform.rotate(self.img_wumpus[1],5)

        self.img_pit = [
            pygame.image.load(os.path.abspath('img/hole.png')),
        ]
        self.img_pit = [pygame.transform.scale(img, (self.part-1,self.part-1)) for img in self.img_pit]

        self.img_gold = [
            pygame.image.load(os.path.abspath('img/gold.png')),
        ]
        self.img_gold = [pygame.transform.scale(img, (self.part-1,self.part-1)) for img in self.img_gold]

        self.img_agent = [
            pygame.image.load(os.path.abspath('img/man.png')),
        ]

        self.img_stench = [
            pygame.image.load(os.path.abspath('img/stench.png')),
        ]

        self.img_breeze = [
            pygame.image.load(os.path.abspath('img/breeze.png')),
        ]

        self.img_agent = [pygame.transform.scale(img, (self.part-1,self.part-1)) for img in self.img_agent]

        self.img_status_agent ={
            "success":pygame.image.load(os.path.abspath('img/success.png')),
            "died": pygame.image.load(os.path.abspath('img/gravestone.png')),
            "got_gold": pygame.image.load(os.path.abspath('img/robber.png')),
            "killed_wumpus":pygame.image.load(os.path.abspath('img/superhero.png')),
            "stench": pygame.image.load(os.path.abspath('img/stench.png')),
            "breeze": pygame.image.load(os.path.abspath('img/breeze.png')),
            "glitter": pygame.image.load(os.path.abspath('img/glitter.png'))
         }

        self.img_status_agent = {
            "success":pygame.transform.scale(self.img_status_agent["success"], (self.part-1,self.part-1)),
            "died": pygame.transform.scale(self.img_status_agent["died"], (self.part-1,self.part-1)),
            "got_gold": pygame.transform.scale(self.img_status_agent["got_gold"], (self.part-1,self.part-1)),
            "killed_wumpus":pygame.transform.scale(self.img_status_agent["killed_wumpus"], (self.part-1,self.part-1)),
            "stench": pygame.transform.scale(self.img_status_agent["stench"], (self.part - 1, self.part - 1)),
            "breeze": pygame.transform.scale(self.img_status_agent["breeze"], (self.part - 1, self.part - 1)),
            "glitter": pygame.transform.scale(self.img_status_agent["glitter"], (self.part - 1, self.part - 1))
        }
    def addAgents(self, agents: list):
        self.agents = agents


    def addWumpus(self, coordinates: list):
        self.wumpus_coordinates = [ self.getPositionElement(x, y) for x, y in coordinates ]

    def addPits(self, coordinates: list):
        #print(coordinates)
        self.pits_coordinates = [ self.getPositionElement(x, y) for x, y in coordinates ]
        #print(self.pits_coordinates)
    def addGold(self, coordinates: list):
        self.gold_coordinates = [ self.getPositionElement(x, y) for x, y in coordinates ]

    def getPositionElement(self, y, x) ->tuple:
        return self.initial_x + (self.part * x), self.square_y - (self.part * y) - self.part

    def moveAgent(self, ):
        pass

    def updateComponents(self, ):
        self.screen.fill(BACKGROUND)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   quit()
        # self.printInfo()

        pygame.draw.line(self.screen, WHITE, (self.initial_x, self.initial_y), (self.initial_x , self.square_y), 2)
        pygame.draw.line(self.screen, WHITE, (self.initial_x, self.initial_y), (self.square_x, self.initial_y), 2)

        for i in range(self.parts):
            pygame.draw.line(self.screen, WHITE, (self.initial_x, self.initial_y  + (self.part * (i+1))),  (self.square_x,  self.initial_y  + (self.part * (i+1))), 4)

        for i in range(self.parts):
            pygame.draw.line(self.screen, WHITE, (self.initial_x  + (self.part * (i+1)), self.initial_y),  (self.initial_x  + (self.part * (i+1)), self.square_y), 2)

        #for coordinate in self.wumpus_coordinates:
        #    self.screen.blit(self.img_wumpus[0], coordinate)

        #for coordinate in self.gold_coordinates:
        #    self.screen.blit(self.img_gold[0], coordinate)

        #for coordinate in self.pits_coordinates:
        #    self.screen.blit(self.img_pit[0], coordinate)

        for coordinate in self.breeze_coord:
            if self.breeze_coord:
                self.screen.blit(self.img_status_agent["breeze"], self.getPositionElement(*coordinate))

        for coordinate in self.stench_coord:
            if self.breeze_coord:
                self.screen.blit(self.img_status_agent["stench"], self.getPositionElement(*coordinate))

        for coordinate in self.glitter_coord:
            if self.breeze_coord:
                self.screen.blit(self.img_status_agent["glitter"], self.getPositionElement(*coordinate))

        agent = self.agents
        if agent.agent_died:
            self.screen.blit(self.img_status_agent["died"], self.getPositionElement(*agent.coordinate))
        elif agent.killedWumpus() and agent.hasGold():
            self.screen.blit(self.img_status_agent["success"], self.getPositionElement(*agent.coordinate))
        elif agent.killedWumpus():
            self.screen.blit(self.img_status_agent["killed_wumpus"], self.getPositionElement(*agent.coordinate))
        elif agent.hasGold():
            self.screen.blit(self.img_status_agent["got_gold"], self.getPositionElement(*agent.coordinate))
        else:
            self.screen.blit(self.img_agent[0], self.getPositionElement(*agent.coordinate))

        if agent.feelBreeze():
            if not agent.coordinate in self.breeze_coord:
                self.breeze_coord.append(agent.coordinate)
                #print(self.breeze_coord)

        if agent.feelStench():
            if not agent.coordinate in self.stench_coord:
                self.stench_coord.append(agent.coordinate)


        if agent.feelGlitter():
            if not agent.coordinate in self.glitter_coord:
                self.glitter_coord.append(agent.coordinate)



        pygame.display.update()

        if self.generation == 'x':
            self.fps = 2
        self.clock.tick(self.fps)


    # def updatePerceptions(self, player: Player):
    #     agent = player
    #     x,y = agent.coordinate
    #     left = x, y-1
    #     right = x, y+1
    #     up = x+1, y
    #     down = x-1, y
    #
    #     for coordinate in self.pits_coordinates:
    #         print(self.pits_coordinates)
    #         if left == coordinate:
    #             print("Pit to left")



    #
    # def printInfo(self,):
    #     font = pygame.font.Font('freesansbold.ttf', 32)
    #     infos = f'Generation {self.generation}'
    #     if self.best_solution:
    #         id_sol, fit_sol = self.best_solution.id, round(self.best_solution.fitness,2)
    #         infos += f' -- Best Solution: ID({id_sol}), Fitness({fit_sol})'
    #     text = font.render(infos, True, WHITE, BACKGROUND)
    #     textRect = text.get_rect()
    #     textRect.center = (self.WIDTH // 2, 25)
    #     self.screen.blit(text, textRect)
