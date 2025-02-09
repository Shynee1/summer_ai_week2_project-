# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import Stack
from util import Queue
from util import PriorityQueue
import searchAgents

class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def build_path(node):
    res = []
    currentNode = node
    while currentNode.parent != None:
        res.insert(0, currentNode.state[1])
        currentNode = currentNode.parent

    return res

def depthFirstSearch(problem: SearchProblem):
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    frontier = Stack()
    visited = []

    frontier.push(Node((problem.getStartState(), None, None), None))
    
    while True:
        currentNode = frontier.pop()
        currentState = currentNode.state

        if problem.isGoalState(currentState[0]):
            return build_path(currentNode)

        visited.append(currentState[0])
        for i in problem.getSuccessors(currentState[0]):
            if i[0] not in visited:
                frontier.push(Node(i, currentNode))

def breadthFirstSearch(problem: SearchProblem):
    frontier = Queue()
    visited = []

    frontier.push(Node((problem.getStartState(), None, None), None))
    
    while True:
        currentNode = frontier.pop()
        currentState = currentNode.state

        if problem.isGoalState(currentState[0]):
            return build_path(currentNode)

        visited.append(currentState[0])
        for i in problem.getSuccessors(currentState[0]):
            if i[0] not in visited:
                frontier.push(Node(i, currentNode))

def uniformCostSearch(problem: SearchProblem):
    frontier = PriorityQueue()
    visited = []

    frontier.push(Node((problem.getStartState(), None, None), None), 0)
    
    while True:
        currentNode = frontier.pop()
        currentState = currentNode.state

        if problem.isGoalState(currentState[0]):
            return build_path(currentNode)

        visited.append(currentState[0])
        for i in problem.getSuccessors(currentState[0]):
            if i[0] not in visited:
                node = Node(i, currentNode)
                frontier.push(node, getTotalCost(node))

def getTotalCost(node):
    if node.parent == None:
        return 0
    return getTotalCost(node.parent) + node.state[2]


def aStarSearch(problem: SearchProblem):
    frontier = PriorityQueue()
    visited = []

    frontier.push(Node((problem.getStartState(), None, None), None), 0)
    
    while True:
        currentNode = frontier.pop()
        currentState = currentNode.state

        if problem.isGoalState(currentState[0]):
            return build_path(currentNode)

        visited.append(currentState[0])
        for i in problem.getSuccessors(currentState[0]):
            if i[0] not in visited:
                node = Node(i, currentNode)
                frontier.push(node, getTotalCost(node) + heuristic(i[0], problem.goal))

def heuristic(position, goal):
    return ((goal[0] - position[0]) ** 2 + (goal[1] - position[1]) ** 2) ** 0.5

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
