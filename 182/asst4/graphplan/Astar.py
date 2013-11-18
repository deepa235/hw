from Pair import Pair
from PropositionLayer import PropositionLayer
from PlanGraph import PlanGraph
from Parser import Parser
from Action import Action
import util
from RelaxedGraphPlan import RelaxedGraphPlan
import time

class DWRProblem(object):
  def __init__(self,domain, problem):
        '''
        Constructor
        '''
        p = Parser(domain, problem)
        domainKB = p.parseActionsAndPropositions();
        self.actions = domainKB[0]
        self.propositions = domainKB[1]
        prob = p.parseProblem()
        self.initialState = prob[0]
        self.goal = prob[1]

  def getActions(self):
    return self.actions

  def getProps(self):
    return self.propositions

  def getStartState(self):
    return self.initialState

  def getGoalState(self):
    return self.goal

  def isGoalState(self, state):
    return all([s in state for s in self.goal])

  def isSubsetOf(self, l1, l2):
    for m in l1:
        if (m not in l2):
            return False
    return True

  def getValidActions(self, actions, state):
    newActions = []
    for action in actions:
      if self.isSubsetOf(action.getPre(), state):
        newActions.append(action)
    return newActions

  
  def getSuccessors(self, state):
    successors = []
    validActions = self.getValidActions(self.actions, state)

    for action in validActions:
      newState = state + [p for p in action.getAdd() if p not in state]
      newState = [p for p in newState if p not in action.getDelete()]
      successors.append((newState, action))
    return successors

def gpHeuristic(state, problem):
  relaxedGP = RelaxedGraphPlan(problem.getActions(), problem.getProps(), (state, problem.getGoalState()))
  return relaxedGP.graphplan()

def contains(first, second):
  for item in first:
    if item not in second:
      return False

  for item in second:
    if item not in first:
      return False

  return True

def aStarSearch(problem, heuristic=gpHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  prioqueue = util.PriorityQueue()
  visited = []

  prioqueue.push((problem.getStartState(), []), 0)
  
  while (not prioqueue.isEmpty()):
    (state, acts) = prioqueue.pop()

    if (problem.isGoalState(state)):
      return acts

    for (succProps, succAct) in problem.getSuccessors(state):
      alreadyVisited = False
      for props in visited:
        if contains(succProps, props):
          alreadyVisited = True

      if not alreadyVisited:
        visited.append(succProps)
        new_acts = acts + [succAct]
        cost = len(new_acts) + heuristic(state, problem)
        prioqueue.push((succProps, new_acts), cost)

  return []

if __name__ == '__main__':
  domain = 'dwrDomain.txt'
  problem = 'dwrProblem.txt'
  gp = DWRProblem(domain, problem)
  before = time.clock()
  plan = aStarSearch(gp)
  after = time.clock()