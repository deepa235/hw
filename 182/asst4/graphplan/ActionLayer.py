'''
Created on Oct 19, 2013

@author: Ofra
'''
from Pair import Pair

class ActionLayer(object):
    '''
    A class for an ActionLayer in a level of the graph. The layer contains a list of actions (action objects) and a list of mutex actions (Pair objects)
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.actions = []
        self.mutexActions = []
        
    def addAction(self, act):
        self.actions.append(act)
        
        
    def removeActions(self, act):
        self.actions.remove(act)
        
    def getActions(self):
        return self.actions
    
    def getMutexActions(self):
        return self.mutexActions
        
    def addMutexActions(self, a1, a2):
        self.mutexActions.append(Pair(a1,a2))
    
    '''returns true if the pair of actions are mutex in this action layer '''
    def isMutex(self, Pair):
        return Pair in self.mutexActions
    
    '''returns true if at least one of the actions in this layer has the proposition prop in its add list '''
    def effectExists(self, prop):
        for act in self.actions:
            if prop in act.getAdd():
                return True
        return False
    
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)
