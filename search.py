# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:45:50 2023

@author: Bijo Sebastian
"""

import operator

def breadthFirstSearch(problem):
  """
  Your search algorithm needs to return a list of actions that reaches the goal
  Strategy: Search the shallowest nodes in the search tree first.
  """
  
  #Create explored list to store popped nodes
  explored = []
  #Create Fringe to store all nodes to be expaned
  fringe = []
  #Add the start state to Fringe 
  fringe.append([problem.getStartState(), [], 0])
  i = 1 #count number of nodes expanded
  
  #Start Breadth First 
  while len(fringe)>0:
      
      #Sort fringe in order of least cost/level
      fringe = sorted(fringe, key = operator.itemgetter(2))
      #Pop least cost node and add to explored list
      current_node = fringe.pop(0)
      i = i+1
      explored.append(current_node[0]) # only the state needs to be added to explored list 
      
      #Check if goal is reached
      if problem.isGoalState(current_node[0]):
          return current_node[1]
      
      #Expand node and get successors 
      for successor, action, step in problem.getSuccessors(current_node[0]):
          
          temp_node = [successor, current_node[1] + [action], current_node[2] + 1] #1 for new cost since BFS do not care
          
          #Check if the successor already exists in explored list
          if successor in explored:
              #If so already optimal do not add to fringe
              continue
          
          #Check if duplicate node exists in fringe
          flag_do_not_append = False
          for node in fringe:        
              if node[0] == successor:                  
                  #Check if existing duplicate is actually shorter path than the new node            
                  if node[2] <= temp_node[2]:
                      #In this case do not add the new node to fringe 
                      flag_do_not_append = True
                      #No need to check further in existing fringe
                      break
          
          if flag_do_not_append:
              #In this case do not add the new node 
              continue
          
          #If none of the above then add successor to fringe 
          fringe.append(temp_node)
  
  return ([])