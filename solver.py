class Solver:
    def __init__(self, filename):
        self.parse(filename)

    def serversInGroup(self, groupnum):
        return filter(lambda serv: serv[2] == groupnum, self.servers)

    def parse(self, filename):
        with open(filename, "r") as f:
            self.rangesNumber, self.slotsPerRange, self.unusedNumber, self.groupsNumber, self.serversNumber = map(int, f.readline().strip().split())

            self.grid = [[-1 for i in range(self.slotsPerRange)] for j in range(self.rangesNumber)]

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
                self.servers.append([s,c,-1,False]) # size, capacity, groupid, isAssigned?

    def sizeLeft(self, i, j):
        for k in range(j, self.slotsPerRange):
            if self.grid[i][k] != -1:
                return k-j
        return self.slotsPerRange - j

    def firstAvailableServerWithSize(self, size):
        i = 0
        while i< len(self.servers):
            server = self.servers[i]
            i+=1
            if server[0] != size: continue
            if server[3] == True : continue
            return i-1
        return -1


if __name__ == "__main__":
    s = Solver("dc.in")
