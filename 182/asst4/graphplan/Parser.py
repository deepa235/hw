'''
Created on Oct 20, 2013

@author: Ofra
'''
from Action import Action
from Proposition import Proposition
class Parser(object):
    '''
    A utility class for parsing the domain and problem.
    '''


    def __init__(self, domainFile, problemFile):
        '''
        Constructor
        '''
        self.domainFile = domainFile
        self.problemFile = problemFile
        

    def parseActionsAndPropositions(self):
        propositions = []
        f = open(self.domainFile, 'r')
        line = f.readline()
        propositionLine = f.readline()
        words = propositionLine.split(" ")
        for i in range(0, len(words)-1):
            propositions.append(Proposition(words[i]))         
        actions = []
        f = open(self.domainFile, 'r')
        line = f.readline()
        while(line != ''):
            words = line.split(" ")
            if(words[0]=='Name:'):
                name = words[1]
                line = f.readline()
                precond = []
                add = []
                delete = []
                words = line.split(" ")
                for i in range(1, len(words)-1):
                    precond.append(Proposition(words[i]))
                line = f.readline()
                words = line.split(" ")
                for i in range(1, len(words)-1):
                    add.append(Proposition(words[i]))
                line = f.readline()
                words = line.split(" ")
                for i in range(1, len(words)-1):
                    delete.append(Proposition(words[i]))   
                act = Action(name,precond,add,delete) 
                for prop in add:
                    self.findPropByName(prop, propositions).addProducer(act)
                actions.append(act)
            line = f.readline()
        return [actions, propositions]
    
    def findPropByName(self, name, propositions):
        for prop in propositions:
            if prop == name:
                return prop
        
   

    
    def parseProblem(self):
        init = []
        goal = []
        f = open(self.problemFile, 'r')
        line = f.readline()
        words = line.split(" ")
        for i in range(2, len(words)-1):
            init.append(Proposition(words[i]))
        line = f.readline()
        words = line.split(" ")
        for i in range(2, len(words)-1):
            goal.append(Proposition(words[i]))            
        return [init, goal]
    
