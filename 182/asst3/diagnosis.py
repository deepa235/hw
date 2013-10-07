'''
Created on Sep 23, 2013

@author: Mark Grozen-Smith
'''

import random

def WalkSAT(clauses,p,max_flips):
    randomize_literals(clauses)
    for i in xrange(max_flips):
        falsies = [clause for clause in clauses if not clause.evaluate()]
        if falsies == []:
            return clauses
        if random.random() < p:
            random_literal = random.choice(random.choice(falsies).literals) #choose a random literal from a random inconsistent clause and flip it
            flip_literal(clauses, random_literal)
        else: 
            pass#ideal_flip(clauses)-flip whichever symbol in clause maximizes the number of satisfed clauses
    return None

def ideal_flip(clauses):
    pass

def flip_literal(clauses, flipped_literal):
    for clause in clauses:
        for literal in clause.literals:
            if  literal.name == flipped_literal.name:
                literal.flip_value()
            

def randomize_literals(clauses):
    literals_seen = {} # dictionary of (keys)literal_names: (values)truth_value
    for clause in clauses:
        for literal in clause.literals:
            if  literal.name in literals_seen.keys():
                literal.value = literals_seen[literal.name]
            else:
                literal.value = random.randrange(0,2)
                literals_seen[literal.name] = literal.value

def print_clauses(clauses):
    print "\n"
    for clause in clauses:
        print clause
    print "\n\n\n\n"

class Literal:
    """Represents a literal"""
    
    def __init__(self, name, negated, value = False):
        self.name = name #literal name
        self.negated = negated #is the literal negated
        self.value = value
    
    def __eq__(self, other):
        return self.name == other.name
    
    def setValue(self, value):
        self.value = value # value of symbol (True or False)
        return self

    def flip_value(self):
        self.value = not self.value

    def setNegated(self, value):
        self.negated = value
        return self
    
    def evaluate(self): #evaluates whether overall the literal is true or false. For example if value = true and negated = false, then the literal will be evaluated as true
        if (self.value and not(self.negated)):
            return True
        elif (not(self.value) and self.negated):
            return True
        return False
    def __str__(self):
        return self.name+";"+str(self.value)
        
class Clause:
    """represents a disjunctive clause"""
    def __init__(self, literals):
        self.literals = literals #a clause is composed of a list of literals with disjunctions between them 
           
    def evaluate(self): #evaluated whether the clause is True or False
        for i in range(len(self.literals)):
            if (self.literals[i].evaluate()):
                return True #since this is a disjunction, one true literal is sufficient
        return False
    def __str__(self):
        str_list = []
        for literal in self.literals:
            str_list.append(str(literal))
        return str(str_list)

if __name__ == '__main__':
    """"your code here: you should create the clauses that form an input to walkSAT and run walkSAT"""
    
    #Literal(name, negated, mutable, value)
    clause1 = Clause([Literal('kidney failure', False)])
    clause2 = Clause([Literal('kidney failure', False), Literal('heart failure', False)])
    clause3 = Clause([Literal('neurological System Failure', False), Literal('blood flow issues', False)])
    clause4 = Clause([Literal('blood flow issues', False), Literal('liver failure', False)])
    clause5 = Clause([Literal('kidney failure', False), Literal('blood flow issues', False)])
    clause6 = Clause([Literal('neurological System Failure', False), Literal('heart failure', False), Literal('kidney failure', False)])

    clauses = [clause1, clause2, clause3, clause4]
    print_clauses(clauses)
    randomize_literals(clauses) 
    print_clauses(clauses)




"""
    coughing = Literal("Coughing", False)
    coughing.setValue(True)
    coughing.setMutable(False)

    fever = Literal("Fever", False)
    fever.setValue(True)
    fever.setMutable(False)

    bloodClot = Literal("Blood Clot", False)
    bloodClot.setValue(True)
    bloodClot.setMutable(False)

    bloodPressure = Literal("Blood Pressure", False)
    bloodPressure.setValue(True)
    bloodPressure.setMutable(False)

    headAche = Literal("Head Ache", False)
    headAche.setValue(True)
    headAche.setMutable(False)

    stomachAche = Literal("Stomach Ache", False)
    stomachAche.setValue(False)
    stomachAche.setMutable(False)
    
    neuroSys = Literal("Neurological System Failure", False)
    neuroSys.setValue(False)
    neuroSys.setMutable(True)

    kidneyFailure = Literal("Kidney Failure", False)
    kidneyFailure.setValue(False)
    kidneyFailure.setMutable(True)

    heartFail = Literal("Heart Failure", False)
    heartFail.setValue(False)
    heartFail.setMutable(True)

    bloodFlow = Literal("Blood Flow Problems", False)
    bloodFlow.setValue(False)
    bloodFlow.setMutable(True)
    """




