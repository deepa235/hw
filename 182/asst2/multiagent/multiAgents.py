# multiAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from util import manhattanDistance
from game import Directions
import random, util
import time

from game import Agent

class ReflexAgent(Agent):
  """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
  """


  def getAction(self, gameState):
    """
    You do not need to change this method, but you're welcome to.

    getAction chooses among the best options according to the evaluation function.

    Just like in the previous project, getAction takes a GameState and returns
    some Directions.X for some X in the set {North, South, West, East, Stop}
    """
    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()

    # Choose one of the best actions
    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best

    "Add more of your code here if you want to"

    return legalMoves[chosenIndex]

  def evaluationFunction(self, currentGameState, action):
    """
    Design a better evaluation function here.

    The evaluation function takes in the current and proposed successor
    GameStates (pacman.py) and returns a number, where higher numbers are better.

    The code below extracts some useful information from the state, like the
    remaining food (oldFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.

    Print out these variables to see what you're getting, then combine them
    to create a masterful evaluation function.
    """
    # Useful information you can extract from a GameState (pacman.py)
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()
    oldFood = currentGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    "*** YOUR CODE HERE ***"
    return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
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
  """
    Your minimax agent (question 2)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action from the current gameState using self.depth
      and self.evaluationFunction.

      Here are some method calls that might be useful when implementing minimax.

      gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

      Directions.STOP:
        The stop direction, which is always legal

      gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

      gameState.getNumAgents():
        Returns the total number of agents in the game
    """
    "*** YOUR CODE HERE ***"

    return self.value(gameState, 0, 0)[0]

  def value(self, gameState, depth, agentIndex):
    if agentIndex >= gameState.getNumAgents():
      depth += 1
      agentIndex = 0


    if depth == self.depth:
      return self.evaluationFunction(gameState)

    if agentIndex == 0:
      return self.maxValue(gameState, depth, agentIndex)
    else:
      return self.minValue(gameState, depth, agentIndex)

  def maxValue(self, gameState, depth, agentIndex):
    returnObject = (Directions.STOP, -1 *float("inf"))

    legalActions = gameState.getLegalActions(agentIndex)
    if not legalActions:
      return self.evaluationFunction(gameState)

    for action in legalActions:
      if action == Directions.STOP:
        continue

      newValue = self.value(gameState.generateSuccessor(agentIndex, action), depth, agentIndex + 1)
      if type(newValue) is tuple:
        newValue = newValue[1]
      if(newValue > returnObject[1]):
        returnObject = (action, newValue)
    return returnObject


  def minValue(self, gameState, depth, agentIndex):
    returnObject = (Directions.STOP, float("inf"))
    legalActions = gameState.getLegalActions(agentIndex)
    if not legalActions:
      return self.evaluationFunction(gameState)

    for action in legalActions:
      if action == Directions.STOP:
        continue

      newValue = self.value(gameState.generateSuccessor(agentIndex, action), depth, agentIndex + 1)
      if type(newValue) is tuple:
        newValue = newValue[1]
      if(newValue < returnObject[1]):
        returnObject = (action, newValue)
    return returnObject

class AlphaBetaAgent(MultiAgentSearchAgent):
  """
    Your minimax agent with alpha-beta pruning (question 3)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action using self.depth and self.evaluationFunction
    """
    "*** YOUR CODE HERE ***"
    return self.value(gameState, 0, 0, -1*float("inf"), float("inf"))[0]

  def value(self, gameState, depth, agentIndex, alpha, beta):
    if agentIndex >= gameState.getNumAgents():
      depth += 1
      agentIndex = 0


    if depth == self.depth or gameState.isWin() or gameState.isLose():
      return self.evaluationFunction(gameState)

    if agentIndex == 0:
      return self.maxValue(gameState, depth, agentIndex, alpha, beta)
    else:
      return self.minValue(gameState, depth, agentIndex, alpha, beta)

  def maxValue(self, gameState, depth, agentIndex, alpha, beta):
    returnObject = (Directions.STOP, -1 *float("inf"))

    legalActions = gameState.getLegalActions(agentIndex)
    if not legalActions:
      return self.evaluationFunction(gameState)

    for action in legalActions:
      if action == Directions.STOP:
        continue

      newValue = self.value(gameState.generateSuccessor(agentIndex, action), depth, agentIndex + 1, alpha, beta)
      if type(newValue) is tuple:
        newValue = newValue[1]
      if(newValue > returnObject[1]):
        returnObject = (action, newValue)

      if returnObject[1] >= alpha:
        alpha = returnObject[1]

      if returnObject[1] >= beta:
        return returnObject

    return returnObject


  def minValue(self, gameState, depth, agentIndex, alpha, beta):
    returnObject = (Directions.STOP, float("inf"))
    legalActions = gameState.getLegalActions(agentIndex)
    if not legalActions:
      return self.evaluationFunction(gameState)

    for action in legalActions:
      if action == Directions.STOP:
        continue

      newValue = self.value(gameState.generateSuccessor(agentIndex, action), depth, agentIndex + 1, alpha, beta)
      if type(newValue) is tuple:
        newValue = newValue[1]
      if newValue < returnObject[1]:
        returnObject = (action, newValue)

      if returnObject[1] <= beta:
        beta = newValue

      if returnObject[1] <= alpha:
        return returnObject

    return returnObject

class ExpectimaxAgent(MultiAgentSearchAgent):
  """
    Your expectimax agent (question 4)
  """

  def getAction(self, gameState):
    """
      Returns the expectimax action using self.depth and self.evaluationFunction

      All ghosts should be modeled as choosing uniformly at random from their
      legal moves.
    """
    "*** YOUR CODE HERE ***"
    return self.value(gameState, 0, 0)[0]

  def value(self, gameState, depth, agentIndex):
    if agentIndex >= gameState.getNumAgents():
      depth += 1
      agentIndex = 0


    if depth == self.depth:
      return self.evaluationFunction(gameState)

    if agentIndex == 0:
      return self.maxValue(gameState, depth, agentIndex)
    else:
      return self.minValue(gameState, depth, agentIndex)

  def maxValue(self, gameState, depth, agentIndex):
    returnObject = (Directions.STOP, -1 *float("inf"))

    legalActions = gameState.getLegalActions(agentIndex)
    if not legalActions:
      return self.evaluationFunction(gameState)

    for action in legalActions:
      if action == Directions.STOP:
        continue

      newValue = self.value(gameState.generateSuccessor(agentIndex, action), depth, agentIndex + 1)
      if type(newValue) is tuple:
        newValue = newValue[1]
      if(newValue > returnObject[1]):
        returnObject = (action, newValue)
    return returnObject


  def minValue(self, gameState, depth, agentIndex):
    returnObject = (Directions.STOP, float("inf"))
    legalActions = gameState.getLegalActions(agentIndex)
    newValue = 0.
    actionCounter = 0.
    if not legalActions:
      return self.evaluationFunction(gameState)

    for action in legalActions:
      if action == Directions.STOP:
        continue

      getValue = self.value(gameState.generateSuccessor(agentIndex, action), depth, agentIndex + 1)
      if type(getValue) is tuple:
        getValue = getValue[1]
      newValue += getValue
      actionCounter += 1.
    returnObject = (action, newValue / actionCounter)
    return returnObject

def betterEvaluationFunction(currentGameState):
  """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>

    The important factors for evaluating a game state are basically what we think about 
    as we play the game.  These factors include how far away from the food we are, 
    how close we are to the ghosts, how close we are to the capsules, and what the
    current score is.  Since a large score is the ultimate goal, that should have a lot of weight.
    On the other hand, being close to the food is only a minor goal in the short term, so that
    has a small weight. Being very close to the ghosts is really scary unless we can eat them
    which gives a lot of points.  In either case, ghost proximity is weighted quite heavily.  


  """
  "*** YOUR CODE HERE ***"
  foodArray = currentGameState.getFood().asList()
  pacmanPosition = currentGameState.getPacmanPosition()
  ghostStates = currentGameState.getGhostStates()
  capsulePositions = currentGameState.getCapsules()


  foodDistance = 0.
  ghostDistance = 0.
  capsuleDistance = 0.
  
  for capsule in capsulePositions:
    capsuleDistance += 10 / float(manhattanDistance(pacmanPosition, capsule))

  for food in foodArray:
    foodDistance += 1 / float(manhattanDistance(pacmanPosition, food))
  food_count = len(foodArray)+1
  foodDistance = foodDistance / food_count

  ghostFactor = 0.
  for ghost in ghostStates:
    ghostPosition = ghost.getPosition()
    if ghostPosition == pacmanPosition:
      return -float("inf")
    if ghost.scaredTimer == 0:
      ghostDistance -= 1 / float(manhattanDistance(pacmanPosition, ghostPosition))
    else:
      ghostDistance += 50 / float(manhattanDistance(pacmanPosition, ghostPosition))

  score = currentGameState.getScore()
  foodDistance = foodDistance
  ghostDistance = 100*ghostDistance
  capsuleDistance = 50*capsuleDistance
  return currentGameState.getScore() + foodDistance + ghostDistance + capsuleDistance



# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
  """
    Your agent for the mini-contest
  """

  def getAction(self, gameState):
    """
      Returns an action.  You can use any method you want and search to any depth you want.
      Just remember that the mini-contest is timed, so you have to trade off speed and computation.

      Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
      just make a beeline straight towards Pacman (or away from him if they're scared!)
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

