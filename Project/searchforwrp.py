import mapsforwrp
import operator
def searcher(maze):
    #Search for a path using 
    # a) Singleton Heuristic
    # b) Minimum Spanning Tree Heuristic
    # c) Travelling Salesman Heuristic
    # may implement JF in addition to work in tandem with the above heuristics
    #paths = search1.searcher(current_maze)
    paths = []
    ##1) Singleton Heuristic
    '''
    Our first heuristic is based on the idea that, in order to solve WRP, the watchman agent
    must see each of the vertices from S.unseen. Thus, for each vertex p ∈ S.unseen (denoted
    as the pivot p) we define its Singleton heuristic to be the minimal distance from S.location
    to a vertex q ∈ LOST o(p). Formally, given a pivot vertex p ∈ S.unseen:
    hp(S) = min
    q∈LOS to(p)
    d(S.location, q) (1)
    where d(x, y) is the cost of the shortest path between vertices x and y. For every p ∈
    S.unseen, hp(S) is admissible because the agent will surely travel to some vertex that has
    LOS to p and hp(S) takes the minimum among all those vertices.
    4.1 Aggregating Singleton Heuristics
    Every possible pivot has its own singleton heuristic. Therefore, we can take the maximum of
    each of these heuristics in order to maintain admissibility (Holte, Felner, Newton, Meshulam,
    & Furcy, 2006). There exist a spectrum of possibilities to decide how many and which pivots
    to use. Naturally, adding more pivots has a diminishing return in terms of accuracy of the
    overall heuristic vs. time overhead. While we tried many combinations, in our experiments
    below we took the extreme case of using all cells in the unseen list as pivots. We calculated
    the singleton heuristic for all of them and took the maximum. We denote this heuristic by
    hSingleton. It is formally defined by:
    hSingleton(S) = max
    p∈S.unseen
    hp(S) (2)
    hSingleton is larger than or equal to any other combination of pivots. hSingleton is first
    fully calculated for the root node. Then, every vertex that is added to seen is removed from
    the set of pivots. 
    '''
    E=[]
    for i in range(maze.l):
        for j in range(maze.w):
            E.append((i,j))
    ##now every vertex in unseen is a pivot
    ##do A* with each pivot
    closed=[]
    #state here is a tuple of the form (i,j,seensofar,actions)
    fringe=[]
    ##initialize the fringe
    fringe.append(maze.start.append(E))
    #state is a tuple of the form (i,j,seensofar,actions,heuristic) in fringe
    while(fringe.__len__()>0):
        ##pop the top node from the queue
        state=fringe.pop(0)
        ##if the node popped's third element and its losfrom add up to the whole set of vertices, then return the actions
        for i in maze.lf[state[0]][state[1]]:
            if i not in state[2]:
                state[2].append(i)

        if state[2]==E:
            return state[3]
        #if not then it is not the wrp set and keep proceeding
        else:
            #expand the popped node by performing all possible actions
            p=0
            ##Case 1 : State is in closed and has a higher seensofar
            for i in closed :
                if i[0]==state[0] and i[1]==state[1] and i[2]>=state[2]:
                    p=1
                    continue
            ##Case 2 : State is in closed and has a lower seensofar
                if i[0]==state[0] and i[1]==state[1] and i[2]<state[2]:
                    closed.remove(i)
                    s=[]
                    s.append(state[0])
                    s.append(state[1])
                    s.append(state[2])
                    s.append(state[3])
                    closed.append(s)
                    p=1
            ##Case 3 : State is not in closed
            if(p!=0) :

                    s.append(state[0])
                    s.append(state[1])
                    s.append(state[2])
                    s.append(state[3])
                    closed.append(s)
                    successors = maze.getSuccessors(state)
                    for succ in successors:
                        

        fringe.sort(key=operator.itemgetter(4))
    return paths
