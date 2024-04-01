#initialise the maze
#define the maze class
import search
#Definitions based on color map
start_id = 1
obstacle_id = 16
fringe_id = 4
free_space_id1 = 3
free_space_id2 = 18
expanded_id = 6


class Maps:
    map_data = []
    l = 0
    w = 0
    start = []
    n=0
    lt={}
    lf={}
    #distance lookup is 4D table
    distlookup=[]
    def dissetter(self):
        self.distlookup = [[[[[] for l in range(self.l)] for k in range(self.w)] for j in range(self.l)] for i in range(self.w)]
        return
    def lfsetter(self) :
        self.lf = [[[] for j in range(self.l)] for i in range(self.w)]
        return
    def ltsetter(self) :
        self.lt = [[[] for j in range(self.l)] for i in range(self.w)]
        return
    
    def setup(self, d) :
        #Set up the map
        #generate 
        #a) LOS from set
        #b) LOS to set - done
        #c) D(u,v) for all u,v in V - done

        print(self.map_data)
        print(self.l)
        print(self.w)
        print(self.start)
        print(self.n)
        print(self.lt)
        print(self.lf)
        print(self.distlookup)

        #d is the distance of visibility
        #cannot see past obstacles
        #los from set
        self.lfsetter()
        for i in range(self.w) :
            for j in range(self.l):
                for k in range(self.w):
                    for m in range(self.l):
                        if(self.visible(i,j,k,m) and self.map_data!=obstacle_id) and ((max(i-k,j-m)<= d and min(i-k,j-m)>=-d)):
                            self.lf[i][j].append((k,m))
                            self.lt[i][j].append((k,m))
                            self.lf[k][m].append((i,j))
                            self.lt[k][m].append((i,j))
                            
        #los to set
        #for each cell, invert the los from set
        self.ltsetter()
        for i in range(self.w) :
            for j in range(self.l):
                for k in self.lf[i][j] :
                    self.lt[k[0]][k[1]].append((i,j))

        #D(u,v) for all u,v in V
        #for each cell, calculate the distance to all other cells
        print("here")
        self.dissetter()
        
        for i in range(self.w) :
            for j in range(self.l):
                for k in range(self.w) :
                    for p in range(self.l):
                        if self.map_data[i][j] != obstacle_id and self.map_data[k][p] != obstacle_id:
                            self.distlookup[i][j][k][p]=search.breadthFirstSearcher(self,i,j,k,p)
                            print(i,j,k,p)
                            print(self.distlookup[i][j][k][p])

        return 0
    
    def visible(self,x1,y1,x2,y2) :
    # Calculate the differences
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        # Determine direction of increments
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1

        # Initialize error
        error = dx - dy

        # Initialize current position
        x = x1
        y = y1

        # Iterate along the line
        while x != x2 or y != y2:
            # Check for obstacle
            if self.map_data[x][y]==obstacle_id:
                return False

            # Calculate error for the next step
            error2 = 2 * error

            # Adjust position based on the error
            if error2 > -dy:
                error -= dy
                x += sx
            if error2 < dx:
                error += dx
                y += sy
        return True
    
    four_neighbor_actions = {'up':[-1, 0], 'down':[1, 0], 'left': [0, -1], 'right': [0, 1]}
    
    def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     
     successors = []
     for action in self.four_neighbor_actions:
         
         #Get indiivdual action
         del_x, del_y = self.four_neighbor_actions.get(action)
         
         #Get successor
         new_successor = [state[0] + del_x , state[1] + del_y]
         new_action = action
         
         # Check for obstacle 
         if self.maze_map.map_data[new_successor[0]][new_successor[1]] == obstacle_id:
             continue 
         
         new_cost = len(state[3])+1    
         successors.append([new_successor, new_action, new_cost])
     return successors

#Maze maps
map_1 = Maps()
map_1.map_data = [
     [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16],         
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16,  3,  3,  3,  3,  3,  3, 16],
     [16, 16, 16, 16, 16, 16, 16, 16, 16,  3,  3,  3, 16,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  1,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16]]
map_1.start = [14, 1]
map_1.l = 20
map_1.w = 16


map_2 = Maps()
map_2.map_data = [
     [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16],         
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],       
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16,  3,  3,  3,  3,  3,  3, 16],
     [16, 16, 16, 16, 16, 16, 16, 16, 16,  3,  3,  3, 16,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  1,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16]]
map_2.start = [16, 1]
map_2.l = 20
map_2.w = 18
map_3 = Maps()
map_3.map_data = [
     [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16],         
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16,  3,  3,  3,  3,  3,  3, 16],
     [16, 16, 16, 16, 16, 16, 16, 16, 16,  3,  3,  3, 16,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16,  1,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3, 16],
     [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16]]
map_3.start = [14, 1]
map_3.l = 20
map_3.w = 16

maps_dictionary = {1:map_1, 2:map_2, 3:map_3}


def Mazesetter(n,d):
    c=Maps()
    c.map_data = maps_dictionary[n].map_data
    c.l = maps_dictionary[n].l
    c.w = maps_dictionary[n].w
    c.start = maps_dictionary[n].start
    c.n = n
    c.setup(d)