##### Filename: util.py
##### Author: {your name}
##### Date: {current date}
##### Email: {your email}

import copy
from collections import deque

## Problem 1

### each row of matrix x is multiplied by each col of matrix y
### each row of x is a separate row of matrix z, col of y -> sep col of z

# get_cols method takes a matrix that is a list of lists 
# where each list is a row of the matrix and returns the same 
# where each list is a column of the original matrix
def get_cols(x):
    result_matrix = []
    num_rows = len(x)
    try:
        x[0] # make sure we aren't trying to get cols of empty list
    except IndexError:
        print "input list does not have any rows"
        return 0
    num_cols = len(x[0])
    for col in xrange(num_cols):
        result_matrix.append([])
        for row in xrange(num_rows):
            result_matrix[col].append(x[row][col])
    return result_matrix

def matrix_multiply(x, y):
    result_matrix = []
    y_cols = get_cols(y)
    for xrow in xrange(len(x)):
        result_matrix.append([])
        for ycol in y_cols:
            product_sum = 0
            for index in xrange(len(x[xrow])):
                product_sum += x[xrow][index]*ycol[index]
            result_matrix[xrow].append(product_sum)
    return result_matrix
            


## Problem 2, 3
from collections import deque
from itertools import imap

class MyQueue(deque):
    def __init__(self):
        self = deque()
    def push(self, val):
        super(MyQueue, self).append(val)
    def pop(self):
        try:
            return super(MyQueue, self).popleft()
        except IndexError:
            return None
    def __eq__(self, other):
        if len(self) != len(other): 
            return False
        return not(False in list(imap(lambda x, y: x==y, self, other)))
    def __ne__(self, other):
        return not (self.__eq__(other))
    def __str__(self):
        disp_list = map(str, self)
        return "[" + ",".join(disp_list) + "]"

### Testing
m = MyQueue()
m.push(5)
m.push(6)
n = MyQueue()
n.push(5)
n.push(6)
if not (n.__eq__(m)):
    print "Test 1 failed - Line 78"

if (n.__ne__(m)):
    print "Test 2 failed - Line 81"
n.pop()
if (n.__eq__(m)):
    print "Test 3 failed - Line 84"
if not (n.__ne__(m)):
    print "Test 4 failed - Line 86"
if m.pop() != 5:
    print "Test 5 failed - Line 88"
if m.pop()!= 6:
    print "Test 6 failed - Line 90"
if m.pop() != None:
    print "Test 7 failed - Line 92"
### end Testing

class MyStack(deque):
    def __init__(self):
        self = deque()
    def push(self, val):
        super(MyStack, self).append(val)
    def pop(self):
        try:
            return super(MyStack, self).pop()
        except IndexError:
            return None
    def __eq__(self, other):
        if len(self) != len(other): 
            return False
        return not(False in list(imap(lambda x, y: x==y, self, other)))

    def __ne__(self, other):
        return not (self.__eq__(other))
    def __str__(self):
        disp_list = map(str, self)
        return "[" + ",".join(disp_list) + "]"

### Testing
m = MyStack()
m.push(5)
m.push(6)
n = MyStack()
n.push(5)
n.push(6)
if not (n.__eq__(m)):
    print "Test 1 failed - Line 124"
if (n.__ne__(m)):
    print "Test 2 failed - Line 126"

n.pop()
if (n.__eq__(m)):
    print "Test 3 failed - Line 130"
if not (n.__ne__(m)):
    print "Test 4 failed - Line 132"
if m.pop() != 6:
    print "Test 5 failed - Line 134"
if m.pop()!= 5:
    print "Test 6 failed - Line 136"
if m.pop() != None:
    print "Test 7 failed - Line 138"
### end Testing


## Problem 4

def add_position_iter(lst, number_from=0):
    ret_list = []
    for index in xrange(len(lst)):
        ret_list.append(lst[index] + index + number_from)
    return ret_list

### Testing
if (add_position_iter([7, 5, 1, 4]) != [7, 6, 3, 7]):
    print "Failed Test 1 - Line 152"

### End Testing

def add_position_recur(lst, number_from=0):
    if (lst == []):
        return []
    elif (len(lst) == 1):
        return [lst[0] + number_from]
    else:
        return [lst[0] + number_from] + map(lambda x: x+1 + number_from, add_position_recur(lst[1:]))

### Testing
a = [1,2,3,4]
if add_position_recur(a) != [1,3,5,7]:
    print "Test 1 failed - Line 165"
if add_position_recur(a, 3) != [4,6,8,10]:
    print "Test 2 failed - Line 167"
### End Testing


# inc_gen is unused, just something I was trying and want to ask about
# tried to make a simple generator to increase by one w each use
# didn't know how to use it with map.  always started over with each call
def inc_gen():
    a = 0
    while True:
        yield a
        a = a+1

def add_position_map(lst, number_from=0):
    list2 = []
    map(lambda x: list2.append(x), lst)
    list2 = map(lambda (x,i): x + i + number_from, enumerate(list2))
    return list2

### Testing
a = [1,2,3,4]
if add_position_map(a) != [1,3,5,7]:
    print "Test 1 failed - Line 179"
if add_position_map(a, 3) != [4,6,8,10]:
    print "Test 2 failed - Line 181"
### End Testing

## Problem 5

def remove_course(roster, student, course):
    roster[student].remove(course)
    return roster

### Testing 
roster = {'kyu': set(['cs182']), 'david': set(['cs182'])}
remove_course(roster, 'kyu', 'cs182')
if roster != {'kyu': set([]), 'david': set(['cs182'])}:
    print "Failed Test 1 - Line 205"
### End Testing

from copy import deepcopy
def deep_copy(roster):
    return deepcopy(roster)

def copy_remove_course(roster, student, course):
    x = remove_course(deep_copy(roster), student, course)
    return x

### Testing
roster = {'kyu': set(['cs182']), 'david': set(['cs182'])}
new_roster = copy_remove_course(roster, 'kyu', 'cs182')
if roster != {'kyu': set(['cs182']), 'david': set(['cs182'])}:
    print "Failed Test 1 - Line 219"
if new_roster != {'kyu': set([]), 'david': set(['cs182'])}:
    print "Failed Test 2 - Line 221"

### End Testing

