#initialise the maze
#define the maze class
import search
#Definitions based on color map
start_id = 1
obstacle_id = 16
fringe_id = 4
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