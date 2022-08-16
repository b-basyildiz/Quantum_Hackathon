import pygame, sys
import time
import itertools
from random import choice, sample
from math import sqrt, ceil

def dist(a, b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


class Creature:

    __id_iter__ = itertools.count()
    def __init__(self, team: bool, a = None, b = None, c = None):
        self.team = team
        self.group = team
        self.genes = {'a': a, 'b': b, 'c': c}
        self.id = next(Creature.__id_iter__)
        self.age = 0

    def breed(self, other):
        offspring = Creature(self.team)
        for ii in self.genes:
            if self.genes[ii] != None and other.genes[ii] == None:
                offspring.genes[ii] = self.genes[ii]
            elif self.genes[ii] == None and other.genes[ii] != None:
                offspring.genes[ii] = other.genes[ii]
            elif self.genes[ii] != None and other.genes[ii] != None:
                offspring.genes[ii] = choice([self.genes[ii], other.genes[ii]])
        numGenes = {True: 0, False: 0}
        for ii in offspring.genes:
            if offspring.genes[ii] != None:
                numGenes[offspring.genes[ii]] += 1
        offspring.team = self.team if numGenes[True] == numGenes[False] else \
            numGenes[True] > numGenes[False]
        offspring.group = self.group

        return offspring

    def print(self):
        print(f'creature id: {self.id}\nteam: {self.team}\ngenes: \
            {self.genes}\ngroup: {self.group}\nage: {self.age}\n')

    def move(self):
        self.group = not self.group

class Entity:
    def __init__(self, team: bool,size, group = None, posx = 0, posy = 0):
        self.creature = Creature(team)
        if group != None:
            self.creature.group = group
        self.posx = posx
        self.posy = posy
        self.size = size
    def makeFromCreature(self, creature, size, posx = 0, posy = 0):
        self.creature = creature
        self.posx = posx
        self.posy = posy
        self.size = size

    def setPos(self, posx = 0, posy = 0):
        self.posx = posx
        self.posy = posy

class Manager:
    def __init__(self, screen, screenWidth, screenHeight, maxRowSize = 5):
        self.entities = []
        self.screen = screen
        self.maxRowSize = maxRowSize
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.numEntities = 0
        self.entitySize = screenWidth/(2*maxRowSize) - screenWidth/30

    def addEntity(self, team, group):
        self.entities.append(Entity(team, self.entitySize, group=group))
        self.numEntities += 1
        self.arrangeEntities()

    def addEntityFromCreature(self, creature):
        newEntity = Entity(False, 0)
        newEntity.makeFromCreature(creature, self.entitySize)
        self.entities.append(newEntity)
        self.numEntities += 1
        self.arrangeEntities()

    def drawEntities(self):
        for entity in self.entities:
            pygame.draw.circle(self.screen, (0, 0, 255) if entity.creature.team \
                else (255, 0, 0), (entity.posx, entity.posy), entity.size)
    
    def getArrangement(self):
        arrangement = []
        trueEntities = []
        falseEntities = []
        for ii in self.entities:
            if ii.creature.group:
                trueEntities.append(ii)
            else:
                falseEntities.append(ii)

        numTrue = len(trueEntities)
        numFalse = len(falseEntities)
        
        trueRows = [0]
        currentCount = 0
        currentRow = 0
        while(numTrue):
            if currentCount == 5:
                currentCount = 0
                currentRow += 1
                trueRows.append(0)
            numTrue -= 1
            currentCount += 1
            trueRows[currentRow] += 1
        falseRows = [0]
        currentCount = 0
        currentRow = 0
        while(numFalse):
            if currentCount == 5:
                currentCount = 0
                currentRow += 1
                falseRows.append(0)
            numFalse -= 1
            currentCount += 1
            falseRows[currentRow] += 1
        



        for ii in range(len(falseRows)):
            for jj in range(falseRows[ii]):
                arrangement.append([self.screenWidth/falseRows[ii]*(jj+0.5), self.screenWidth/self.maxRowSize * (ii+1/2), False])
       
        for ii in range(len(trueRows)):
            for jj in range(trueRows[ii]):
                arrangement.append([self.screenWidth/trueRows[ii]*(jj+0.5), self.screenWidth-self.screenWidth/self.maxRowSize * (ii+1/2), True])
         
        return arrangement

    def arrangeEntities(self):
        arrangement = self.getArrangement()
        newPositions = [None] * self.numEntities
        for ii in arrangement:
            minDistance = 10000000000
            best = None
            for kk in range(self.numEntities):
                if dist((self.entities[kk].posx, self.entities[kk].posy), (ii[0], ii[1])) < minDistance \
                    and newPositions[kk] == None and self.entities[kk].creature.group == ii[2]:
                    best = kk
                    minDistance = dist((self.entities[kk].posx, self.entities[kk].posy), (ii[0], ii[1]))
            newPositions[best] = ii

        for ii in range(self.numEntities):
            self.entities[ii].setPos(newPositions[ii][0], newPositions[ii][1])

    def breed(self):
        trueEntities = []
        falseEntities = []
        for ii in self.entities:
            if ii.creature.group:
                trueEntities.append(ii)
            else:
                falseEntities.append(ii)
        trueBreeders = []
        falseBreeders = []
        if len(trueEntities) >= 2:
            trueBreeders = sample(trueEntities, 2)
        if len(falseEntities) >= 2:
            falseBreeders = sample(falseEntities, 2)
        if trueBreeders:
            self.addEntityFromCreature(Creature.breed(trueBreeders[0].creature, \
                trueBreeders[1].creature))
        if falseBreeders:
            self.addEntityFromCreature(Creature.breed(falseBreeders[0].creature, \
                falseBreeders[1].creature))
        self.arrangeEntities()


def main():

    screenWidth = 600
    screenHeight = 900

    pygame.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    manager = Manager(screen, screenWidth, screenHeight)

    manager.addEntity(True, group=True)
    manager.addEntity(True, group=True)
    manager.addEntity(True, group=True)
    manager.addEntity(True, group=True)
    manager.addEntity(True, group=True)
    manager.addEntity(False, group=False)
    manager.addEntity(False, group=False)
    manager.addEntity(False, group=False)
    manager.addEntity(False, group=False)
    manager.addEntity(False, group=False)



    maxRowSize = 10
    blobGap = screenWidth/60

    blobWidth = screenWidth/maxRowSize - (2*blobGap)






    clicked = None
    activeCreature = None
    currentTurn = True
    moveCounter = False

    while(True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for ii in manager.entities:
                    if sqrt((ii.posx-pos[0])**2+(ii.posy-pos[1])**2) < blobWidth/2+blobGap:
                        clicked = ii

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for ii in manager.entities:
                    if sqrt((ii.posx-pos[0])**2+(ii.posy-pos[1])**2) < blobWidth/2+blobGap:
                        if ii == clicked:
                            print(clicked)
                            if ii.creature.team == currentTurn:
                                ii.creature.move()
                                currentTurn = not currentTurn
                                if moveCounter:
                                    manager.breed()
                                moveCounter = not moveCounter
                clicked = None


        screen.fill((255, 255, 255))
        manager.arrangeEntities()
        manager.drawEntities()
        #for ii in range(len(trueArrangement)):
        #    pygame.draw.circle(screen, (0, 0, 255), (trueArrangement[ii][0], trueArrangement[ii][1]), blobWidth/2)
        #   pygame.draw.circle(screen, (255, 0, 0), (falseArrangement[ii][0], falseArrangement[ii][1]), blobWidth/2)
        pygame.display.flip()


    c1 = Creature(False, a = False)
    c2 = Creature(False)
    c3 = Creature(True, a = True, b = True)
    c4 = Creature(True)
    
    babies = [Creature.breed(c1, c3) for ii in range(5)]
    for ii in babies:
        ii.print()


if __name__ == '__main__':
    main()
