'''
Created on Oct 19, 2013

@author: Ofra
'''

class Action(object):
    '''
    The action class is used to define operators. Each action has a list of preconditions, an "add list" of positive effects,
    a "delete list" for negative effects, and the name of the action. The lists for preconditions and effects are lists of Proposition objects.
    '''


    def __init__(self,name,pre,add,delete):
        '''
        Constructor
        '''
        self.pre = pre 
        self.add = add
        self.delete = delete
        self.name = name
        
    def getPre(self):
        return self.pre
    
    def getAdd(self):
        return self.add
    
    def getDelete(self):
        return self.delete
    
    def getName(self):
        return self.name
    
    def isPreCond(self, prop):
        return prop in self.pre
    
    '''returns true if the proposition prop is a positive effect of the action '''
    def isPosEffect(self, prop): 
        return prop in self.add
    
    '''returns true if the proposition prop is a negative effect of the action '''
    def isNegEffect(self, prop):
        return prop in self.delete
    
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.name == other.name)

    def __str__(self):
        return self.name
    
    def __ne__(self, other):
        return not self.__eq__(other)