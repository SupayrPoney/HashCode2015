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
                self.grid[r][s] = "x"

            # all servers
            self.servers = []
            while True:
                line = f.readline()
                if not line : break
                s, c = map(int, line.strip().split())
                self.servers.append([s,c,-1])

    def sizeLeft(self, i, j):
        freespacesleft = 0
        while j < self.slotsPerRange and self.grid[i][j] != "x":
            freespacesleft+=1
            j+=1
        return freespacesleft

if __name__ == "__main__":
    Solver("dc.in")
