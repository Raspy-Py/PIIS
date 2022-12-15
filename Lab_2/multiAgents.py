# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        legalMoves = gameState.getLegalActions()

        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)

        return legalMoves[chosenIndex]

    def scoreDistancesHelper(self, array, pos):
        best = 1000000
        for item in array:
            current = abs(pos[0] - item[0]) + abs(pos[1] - item[1])
            if best > current:
                best = current
        return best

    def ghostDistancesHelper(self, array, pos):
        best = 1000000
        for item in array:
            iPos = item.configuration.pos
            current = abs(pos[0] - iPos[0]) + abs(pos[1] - iPos[1])
            if best > current:
                best = current
        return best

    def ghostNextHelper(self, array, pos):
        for item in array:
            if item.configuration.pos == pos:
                return True
        return False

    def evaluationFunction(self, currentGameState: GameState, action):
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        "*** YOUR CODE HERE ***"
        currentCapsuls = currentGameState.getCapsules()
        successorCapsuls = successorGameState.getCapsules()

        SMALL = 150
        MEDIUM = 300
        LARGE = 500

        currentScore = successorGameState.getScore()
        currentFoodAsList, successorFoodAsList = currentGameState.getFood().asList(), newFood.asList()
        currentPos = currentGameState.getPacmanPosition()
        currentDistanceToFood = self.scoreDistancesHelper(currentFoodAsList, currentPos)
        successorDistanceToFood = self.scoreDistancesHelper(successorFoodAsList, newPos)

        currentDistanceToCapsule = self.scoreDistancesHelper(currentCapsuls, currentPos)
        successorDistanceToCapsule = self.scoreDistancesHelper(successorCapsuls, newPos)

        if successorDistanceToFood < currentDistanceToFood:
            currentScore += (1/successorDistanceToFood) * MEDIUM

        isGhostNext = self.ghostNextHelper(newGhostStates, newPos)
        if isGhostNext:
            currentScore -= LARGE
        return currentScore

def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    def minimax(self, agent, depth, gameState: GameState):
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return self.evaluationFunction(gameState), None
        if agent == 0:
            legalMoves = gameState.getLegalActions(agent)
            bestMax = -100000
            bestMove = "Stop"
            for move in legalMoves:
                successor = gameState.generateSuccessor(agent, move)
                bestMax = max(bestMax, self.minimax(agent + 1, depth, successor)[0])
                if bestMax == self.minimax(agent + 1, depth, successor)[0]:
                    bestMove = move
            return bestMax, bestMove
        else:
            legalMoves = gameState.getLegalActions(agent)
            bestMin = 100000
            bestMove = None
            nextAgent = agent + 1
            numOfAgents = gameState.getNumAgents()
            if agent == numOfAgents - 1:
                nextAgent = 0
                depth += 1
            for move in legalMoves:
                successor = gameState.generateSuccessor(agent, move)
                bestMin = min(bestMin, self.minimax(nextAgent, depth, successor)[0])
                if bestMin == self.minimax(nextAgent, depth, successor)[0]:
                    bestMove = move
            return bestMin, bestMove


    def getAction(self, gameState: GameState):

        return self.minimax(0, 0, gameState)[1]


class AlphaBetaAgent(MultiAgentSearchAgent):
    def minimax(self, agent, depth, gameState: GameState, alpha, beta):
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return self.evaluationFunction(gameState), None
        if agent == 0:
            legalMoves = gameState.getLegalActions(agent)
            bestMax = -10000
            bestMove = "Stop"
            for move in legalMoves:
                successor = gameState.generateSuccessor(agent, move)
                bestMax = max(bestMax, self.minimax(agent + 1, depth, successor, alpha, beta)[0])
                if bestMax == self.minimax(agent + 1, depth, successor, alpha, beta)[0]:
                    bestMove = move
                alpha = max(alpha, bestMax)
                if alpha > beta:
                    break
            return bestMax, bestMove
        else:
            legalMoves = gameState.getLegalActions(agent)
            bestMin = 10000
            bestMove = None
            nextAgent = agent + 1
            numOfAgents = gameState.getNumAgents()
            if agent == numOfAgents - 1:
                nextAgent = 0
                depth += 1
            for move in legalMoves:
                successor = gameState.generateSuccessor(agent, move)
                bestMin = min(bestMin, self.minimax(nextAgent, depth, successor, alpha, beta)[0])
                if bestMin == self.minimax(nextAgent, depth, successor, alpha, beta)[0]:
                    bestMove = move
                beta = min(beta, bestMin)
                if alpha > beta:
                    break
            return bestMin, bestMove

    def getAction(self, gameState: GameState):
        return self.minimax(0, 0, gameState, -999, 999)[1]

class ExpectimaxAgent(MultiAgentSearchAgent):
    def expectimax(self, agent, depth, gameState: GameState):
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return self.evaluationFunction(gameState), None
        if agent == 0:
            legalMoves = gameState.getLegalActions(agent)
            bestMax = -10000
            bestMove = "Stop"
            for move in legalMoves:
                successor = gameState.generateSuccessor(agent, move)
                bestMax = max(bestMax, self.expectimax(agent + 1, depth, successor)[0])
                if bestMax == self.expectimax(agent + 1, depth, successor)[0]:
                    bestMove = move
            return bestMax, bestMove
        else:
            legalMoves = gameState.getLegalActions(agent)
            sumOfChildren = 0
            numOfChildren = len(legalMoves)

            numOfAgents = gameState.getNumAgents()
            nextAgent = agent + 1
            if agent == numOfAgents - 1:
                nextAgent = 0
                depth += 1
            for move in legalMoves:
                successor = gameState.generateSuccessor(agent, move)
                tempMin = self.expectimax(nextAgent, depth, successor)[0]
                sumOfChildren += tempMin
            expectedMin = sumOfChildren / numOfChildren
            return expectedMin, None

    def getAction(self, gameState: GameState):
        return self.expectimax(0, 0, gameState)[1]

        # util.raiseNotDefined()

def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
