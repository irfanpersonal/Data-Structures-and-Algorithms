# What are Data Structures and Algorithms?

# Data Structures define how data is organized, managed, and stored, allowing 
# for efficient access and modification. Different scenarios may require different 
# data structures, so understanding various types helps you choose the best one 
# for a specific task.

# An Algorithm is a set of steps or rules designed to perform a specific task 
# or solve a problem. They outline a systematic approach to achieve a desired 
# outcome.

# Data Structures

# Important - Before we can get started learning Data Structures its important 
# to understand that not all programming languages have support for them right 
# out of the box. 

# What does this mean? You have to implement these data structures yourself.
# And some of these implementations you create by yourself may not be the most
# efficient. You will find that for some of these Data Structures you may 
# choose one over the other even if the current one works with no problems. 

# Important - its also very important to memorize the following Time 
# Complexities.
# O(1) - 1st Place
# O(log n) - 2nd Place
# O(n) - 3rd Place
# O(n log n) - 4th Place
# O(n^2) - 5th Place
# O(2^n) - 6th Place
# O(n!) - 7th Place
# So the 1st place means it is the fastest in performing the task. Meaning
# this is what you should aim for always as its the best #1. And O(n!) is
# last place so the worst, its super slow in performing the task.

# 1st Data Structure - Stack

# A Stack is a "LIFO" data structure meaning "Last In First Out".

# In Python we don't have a "Stack" built in so we will create one ourself.
# The 2 main ways of creating the "Stack" data structure in Python are:
# 1st - list
# 2nd - collections.deque

# Stack Implementation Requirements
# push() - add item to top of stack
# pop() - remove item at top of stack
# peek() -  return the top value on stack
# isEmpty() - returns a boolean indicating if empty
# size() - returns amount of values in array

# 1st Implementation of "Stack" using "list"

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            raise IndexError(f"You cannot remove the top element of a stack if the stack is empty!")

    def peek(self):
        if self.stack:
            return self.stack[len(self.stack) - 1]
        else:
            raise IndexError(f"You cannot get the top value of the stack if its empty!")
    
    def isEmpty(self):
        return False if len(self.stack) else True
    
    def size(self):
        return len(self.stack)
    
    def __repr__(self):
        return f"Stack({self.stack})"
    
# Now this approach works but its not the best implementation as a "list" 
# can run into speed issues as it grows. Because behind the scenes when you 
# create a list it takes a set amount of space in memory. So as your "list" 
# grows larger than that set amount it will have to increase its set amount.
# Which means creating a new larger set amount of space in memory and copying
# over all its elements to the new one. This explains why sometimes when 
# you use the "append" method it may take longer than the other times you
# have used it.

# The alternative implementation is using a "deque", where "de" stands for 
# "double ended". You can find it in "collections" which is built into Python. 
# The reason why "deque" is better is because of its "O(1)" time complexity 
# for adding something to the very begining and removing something from the
# very beginning. Whereas a "list" would have to do some "shifting" of all the 
# elements for both adding something to the very beginning and removing 
# something from the very beginning which gives it a "O(n)" time complexity. 

# 2nd Implementation of "Stack" using "collections.deque"

from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.appendleft(value)

    def pop(self):
        if self.stack:
            self.stack.popleft()
        else:
            raise IndexError(f"You cannot remove the top element of a stack if the stack is empty!")
        
    def peek(self):
        if self.stack:
            return self.stack[0]
        else:
            raise IndexError(f"You cannot get the top value of the stack if its empty!")
    
    def isEmpty(self):
        return False if len(self.stack) else True
    
    def size(self):
        return len(self.stack)
    
    def __repr__(self):
        return f"Stack({self.stack})"
    
# Now lets discuss real world scenarios where you will see the use of a "Stack"
# data structure. In your browser you may find yourself using left and right 
# arrows to navigate back and forth. This is created using a "Stack". 

# 2nd Data Structure - Queue

# A Queue is a "FIFO" data structure meaning "First In First Out".

# In Python we don't have a "Queue" built in so we will create one ourself.
# The 2 main ways of creating the "Queue" data structure in Python are:
# 1st - list
# 2nd - collections.deque

# Queue Implementation Requirements
# enqueue - add element to end of queue
# dequeue - remove and return first element of queue
# front - return first element in queue (so whos next)
# isEmpty - boolean indicating if queue is empty
# size() - returns amount of values in queue

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            raise IndexError('You cannot remove and return the first element of the queue if its empty!')
        
    def peek(self):
        if self.queue:
            return self.queue[0]
        else:
            raise IndexError('You cannot get the first element in the queue if its empty!')
        
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def __repr__(self):
        return f"Queue({self.queue})"
    
# 2nd Implementation of "Queue" using "collections.deque"

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        else:
            raise IndexError('You cannot remove and return the first element of the queue if its empty!')
        
    def peek(self):
        if self.queue:
            return self.queue[0]
        else:
            raise IndexError('You cannot get the first element in the queue if its empty!')
        
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def __repr__(self):
        return f"Queue({self.queue})"
    
# Now lets discuss real world scenarios where you will see the use of a "Queue"
# data structure. When you enter some input using the keyboard its important 
# that the letters appear on the screen in the order they are pressed.

# 3rd Data Structure - Priority Queue

# 2723 3564          4287 7989

# 1932 5660         7679 1605

# 7679 7009         6271 3540

# 5372 2121          7458 4321
 
# 0073 2063          7225 8092   