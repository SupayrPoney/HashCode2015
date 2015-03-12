from solver import Solver

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

def compact():
    for i in irange(0):
        for j in jrange(0):
            if solver.grid[i][j] == -1:
                for k in range(j+1, solver.slotsPerRange):
                    if solver.grid[i][k] == 'x':
                        if k > j+1:
                            solver.grid[i][k-1] = -1
                        break
                    solver.grid[i][k-1] = solver.grid[i][k]

# Sort servers by decreasing size
#solver.servers.sort(key=lambda s: -s[0])

# Sort servers by perf/size ratio decreasing
solver.servers.sort(key=lambda s: float(-s[1])/s[0])

def main(g=0):
    for id in range(len(solver.servers)):
        serv = solver.servers[id]
        if serv[3]:
            continue
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
    print "\033[1;31mYOU WIN", solver.getScore(), "\033[0mMax hole size:", solver.maxHoleSize()
    solver.saveOutput()
    return g

if __name__ == "__main__":
    g = main()
    print solver.grid[0]
    compact()
    print solver.grid[0]
    print "\033[1;31mYOU WIN", solver.getScore(), "\033[0mMax hole size:", solver.maxHoleSize()
    
    main(g)
