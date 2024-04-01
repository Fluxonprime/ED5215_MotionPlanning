
#import necessities
import mapsforwrp
import searchforwrp 
d=int(input("Enter the d Visibilty of the WRP: "))
n=int(input("Enter the maze number: "))
current_maze = mapsforwrp.Mazesetter(n,d)
#Search for a path using 
# a) Singleton Heuristic
# b) Minimum Spanning Tree Heuristic
# c) Travelling Salesman Heuristic
# may implement JF in addition to work in tandem with the above heuristics
#paths = search1.searcher(current_maze)
'''    for path in paths:
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
'''