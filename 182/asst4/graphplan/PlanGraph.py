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


class PlanGraph(object):
    '''
    A class for representing a level in the plan graph. For each level i, the PlanGraph consists of the actionLayer and propositionLayer at this level
    '''


    def __init__(self, level, independentActions):
        '''
        Constructor
        '''
        self.level = level
        self.independentActions = independentActions # a list of the independent actions (this would be the same at each level)
        self.actionLayer = ActionLayer()
        self.propositionLayer = PropositionLayer();
    
    def getPropositionLayer(self):
        return self.propositionLayer
    
    def setPropositionLayer(self, propLayer):
        self.propositionLayer = propLayer    
    
    def getActionLayer(self):
        return self.actionLayer

    def setActionLayer(self, actLayer):
        self.actionLayer = actLayer  

    def are_all_Mutex(self,pre, props):
        for prop1, prop2 in combinations(pre,2):
            if props.isMutex(prop1, prop2):
                return True
        return False
    
    def expand(self, previousLevel, allProps, allActions): #you can change the params the function takes if you like
        Pk = PropositionLayer()
        Ak = ActionLayer()

        for action in allActions:
            pre = action.getPre()
            if not (False in [(item1 in previousLevel.getPropositionLayer().getPropositions()) for item1 in pre]):
                if (not self.are_all_Mutex(pre, previousLevel.getPropositionLayer())):
                    Ak.addAction(action)

        for (action1,action2) in combinations(Ak.getActions(), 2):
            if action1 != action2:
                if previousLevel.mutexActions(action1, action2, previousLevel.getPropositionLayer().getMutexProps()):
                    Ak.addMutexActions(action1, action2)

        
        for prop in allProps:
            for action in Ak.getActions():
                if action.isPosEffect(prop):
                    Pk.addProposition(prop)
        
        for (prop, prop2) in combinations(Pk.getPropositions(), 2):
            if (prop != prop2) and (self.mutexPropositions(prop, prop2, Ak.getMutexActions())):
                Pk.addMutexProp(prop, prop2)


        self.setPropositionLayer(Pk)
        self.setActionLayer(Ak)
            
                
    def mutexActions(self, a1, a2, mutexProps):
        '''YOUR CODE HERE: complete code for deciding whether actions a1 and a2 are mutex, given the previous proposition layer. Your exapnd function should call this function'''
        
        if Pair(a1, a2) not in self.independentActions:
            return True
        for pre_1 in a1.getPre():
            for pre_2 in a2.getPre():
                if Pair(pre_1, pre_2) in mutexProps:
                    return True
        return False
    
    def mutexPropositions(self, prop1, prop2, mutexActions):
        '''YOUR CODE HERE: complete code for deciding whether propositions p1 and p2 are mutex, given the previous proposition layer. Your exapnd function should call this function'''
        for prod_1 in prop1.getProducers():
            for prod_2 in prop2.getProducers():
                if Pair(prod_1, prod_2) not in mutexActions:
                    return False
        return True







