'''
Created on Oct 20, 2013

@author: Ofra
'''
from Action import Action
from ActionLayer import ActionLayer
from Pair import Pair
from Proposition import Proposition
from PropositionLayer import PropositionLayer
from itertools import combinations

class RelaxedPlanGraph(object):
    '''
    A class for representing a level in the plan graph. For each level i, the PlanGraph consists of the actionLayer and propositionLayer at this level
    '''


    def __init__(self, level):
        '''
        Constructor
        '''
        self.level = level
        self.actionLayer = ActionLayer()
        self.propositionLayer = PropositionLayer()
    
    def getPropositionLayer(self):
        return self.propositionLayer
    
    def setPropositionLayer(self, propLayer):
        self.propositionLayer = propLayer    
    
    def getActionLayer(self):
        return self.actionLayer

    def isSubsetOf(self, l1, l2):
        for m in l1:
            if (m not in l2):
                return False
        return True
    
    def expand(self, previousLevel, allProps, allActions): #you can change the params the function takes if you like
        propositionList = self.getPropositionLayer()
        actionList = self.getActionLayer()

        for action in allActions:
            precondition = action.getPre()
            if self.isSubsetOf(precondition, previousLevel.propositionLayer.getPropositions()):
                actionList.addAction(action)

        for proposition in allProps:
            if actionList.effectExists(proposition):
                propositionList.addProposition(proposition)

        self.setPropositionLayer(propositionList)
        self.actionLayer = actionList
