# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:45:50 2023

@author: Bijo Sebastian
"""


"""
Implement your search algorithms here
"""
'''
function TREE-SEARCH( problem, strategy) returns a solution, or failure
create empty fringe and closed set
add the initial state of problem to fringe
loop do
if there are no candidates for expansion in the fringe then return failure
pop a node for expansion from fringe according to strategy
add the popped node to closed set
if the popped node is goal state, then return the corresponding solution
else
expand the popped node by performing all possible actions
for each resulting child node:
add the child node to the fringe
except:
if child node exists in closed set
if duplicate child node exists in fringe:
store the one that can be reached via shorter path from start node
'''
import operator
import maze_maps
import maze_bfs

def breadthFirstSearcher(problem,i,j,k,l):
  """
  Your search algorithm needs to return a list of actions that reaches the goal
  Strategy: Search the shallowest nodes in the search tree first.
  """
  "*** YOUR CODE HERE ***"
  #problem here is the instance of the class Maze and not Maze1

  problem=maze_bfs.Maze1(problem.n)
    #initialize the stack
  closed = []
  fringe = []
  problem.setstart(i,j)
  problem.setgoal(k,l)
  #push the start node to the stack
  fringe.append((problem.getStartState(), []))
  while fringe:
    #pop the top node from the queue
    state, actions = fringe.pop(0)
    #if the node is the goal state, return the actions
    if problem.isGoalState(state):
      return actions
    #if the node is not the goal state, add it to the closed list
    else :
      #expand the popped node by performing all possible actions
      if state not in closed:
        closed.append(state)
        successors = problem.getSuccessors(state)
        for succ in successors:
          #the child node to the fringe if it is not in the closed list
          if succ[0] not in closed:
          #if the child node is in the fringe, store the one that can be reached via shorter path from start node
            if succ[0] in fringe:
              #store the one that can be reached via shorter path from start node
              #pop the node from the fringe
              for i in range(len(fringe)):
                if fringe[i][0] == succ[0]:
                  if len(fringe[i][1]) > len(actions + [succ[1]]):
                    fringe.pop(i)
                    fringe.append((succ[0], actions + [succ[1]]))
            else:
              fringe.append((succ[0], actions + [succ[1]]))
  return []