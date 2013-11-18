'''
Created on Oct 20, 2013

@author: Ofra
'''
from Pair import Pair
import copy
from PropositionLayer import PropositionLayer
from Parser import Parser
from Action import Action
from RelaxedPlanGraph import RelaxedPlanGraph

class RelaxedGraphPlan(object):
    '''
    A class for initializing and running the graphplan algorithm
    '''


    def __init__(self,actions, props, problem):
        '''
        Constructor
        '''
        self.graph = []
        self.actions = actions
        self.propositions = props
        self.initialState = problem[0]
        self.goal = problem[1]
        self.createNoOps() #creates noOps that are used to propogate existing propositions from one layer to the next
        
    '''the graphplan algorithm. If it's easier for you to write your own code, go for it. But you may use this. The code calls the extract function which you should complete below '''    
    def graphplan(self):
        
        initState = self.initialState
        goalState = self.goal
        level = 0
        
        #create first layer of the graph, note it only has a proposition layer which consists of the initial state.
        propLayerInit = PropositionLayer()
        for prop in initState:
            propLayerInit.addProposition(prop)
        pgInit = RelaxedPlanGraph(0)
        pgInit.setPropositionLayer(propLayerInit)
        self.graph.append(pgInit)
        
        '''while the layer does not contain all of the propositions in the goal state, or some of these propositions are mutex in the layer we, and we have not reached the fixed point, continue expanding the graph'''
        while((self.goalStateNotInPropLayer(goalState, self.graph[level].getPropositionLayer().getPropositions()))):
            level = level +1
            pgNext = RelaxedPlanGraph(level) #create new PlanGraph object
            pgNext.expand(self.graph[level-1], self.propositions, self.actions) #calls the expand function, which you are implementing in the PlanGraph class
            self.graph.append(copy.deepcopy(pgNext)) #appending the new level to the plan graph
        
        return level
    
    '''helper function that checks whether all propositions of the goal state are in the current graph level'''
    def goalStateNotInPropLayer(self, goalState, propositions):
        for goal in goalState:
            if goal not in propositions:
                return True
        return False
    
    '''creates the noOps that are used to propogate propositions from one layer to the next'''
    def createNoOps(self):
        for prop in self.propositions:
            name = prop.name
            precon = []
            add = []
            precon.append(prop)
            add.append(prop)
            delete = []
            act = Action(name,precon,add,delete)
            self.actions.append(act)
            prop.addProducer(act)
