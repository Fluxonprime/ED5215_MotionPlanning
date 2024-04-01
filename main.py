# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:45:50 2023

@author: Bijo Sebastian
"""

import search
import maze

if __name__ == '__main__':
    
    current_maze = maze.Maze(3)
    path = search.breadthFirstSearch(current_maze)
    if path:
        #Check path validity
        row,col = current_maze.getStartState()[:-1] 
        for action in path:
            del_x, del_y = current_maze.four_neighbor_actions.get(action)
            row = row + del_x
            col = col + del_y
            if maze.enable_plots:
                #Update changes on the plot copy
                current_maze.map_plot_copy[row][col] = 10
        if current_maze.isGoalState([row, col, True]):
            print('Found a path of %d moves' % (len(path))) 
            current_maze.plot_map()
        else:
            print('Not a valid path')
        
    else:        
        print("Could not find a path")  

    
 