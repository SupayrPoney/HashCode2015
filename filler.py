from solver import Solver
from random import shuffle

size = lambda server: server[0]
capa = lambda server: server[1]
group = lambda server: server[2]

hasgroup = lambda server: group(server) > -1
solver = Solver("dc.in")

def modrange(min, max, mod):
    for i in range(min, max):
        yield i%mod

def irange(i):
    return modrange(i, i+solver.rangesNumber, solver.rangesNumber)

def jrange(j):
    return modrange(j, j+solver.slotsPerRange, solver.slotsPerRange)

def main():
    g = 0
    for id in range(len(solver.servers)):
        serv = solver.servers[id]
        placed = False
        for i in irange(id):
            if placed:
                break
            for j in jrange(id):
                if placed:
                    break
                if solver.sizeLeft(i, j) >= size(serv):
                    for k in range(j, j+size(serv)):
                        solver.grid[i][k] = id
                    solver.servers[id][2] = g
                    solver.servers[id][3] = True
                    print "Placed", solver.servers[id], "at", i, j
                    g = (g + 1)%solver.groupsNumber
                    placed = True


    print len(filter(lambda s: s[3], solver.servers)), "servers places"
    print len(filter(lambda s: not s[3], solver.servers)), "servers a placer"
    print solver
    print "\033[1;31mYOU WIN", solver.getScore(), "\033[0m"

if __name__ == "__main__":
    main()
