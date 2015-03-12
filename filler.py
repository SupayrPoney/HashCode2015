from solver import Solver
from random import shuffle

size = lambda server: server[0]
capa = lambda server: server[1]
group = lambda server: server[2]

hasgroup = lambda server: group(server) > -1

solver = Solver("dc.in")
i, j, g = 0, 0, 0

shuffle(solver.servers)

for id in range(len(solver.servers)):

    serv = solver.servers[id]
    while j < solver.slotsPerRange and solver.grid[i][j] != -1:
        j += 1

    if solver.sizeLeft(i, j) >= size(serv):
        for k in range(j, j+size(serv)):
            solver.grid[i][k] = id
        solver.servers[id][2] = g
        print "Place", solver.servers[id], "at", i, j
        g = (g + 1)%solver.groupsNumber
        j += size(serv)

    elif j + size(serv) >= solver.slotsPerRange:
        i, j = (i+1)% solver.rangesNumber, 0

print len(solver.servers) - len(solver.serversInGroup(-1)), "servers places"
print solver.getScore()
