class Solver:
    def __init__(self, filename):
        self.parse(filename)

    def parse(self, filename):
        with open(filename, "r") as f:
            self.rangesNumber, self.slotsPerRange, self.unusedNumber, self.groupsNumber, self.serversNumber = map(int, f.readline().strip().split())

            self.grid = [[0 for i in range(self.slotsPerRange)] for j in range(self.rangesNumber)]

            # unavailable spots
            for i in range(self.unusedNumber):
                r, s = map(int, f.readline().strip().split())
                self.grid[r][s] = "X"

            # all servers
            self.servers = []
            for i in range(self.rangesNumber-self.unusedNumber):
                s, c = map(int, f.readline().strip().split())
                self.servers.append((s,c))


   

a= Solver("dc.in")
print a.rangesNumber