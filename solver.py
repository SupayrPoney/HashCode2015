class Solver:
    def __init__(self, filename):
        self.parse(filename)

    def serversInGroup(self, groupnum):
        return filter(lambda serv: serv[2] == groupnum, self.servers)

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


    def getServIngroupInRow(self,group,row):
        res=[]
        i=0

        while (i<self.slotsPerRange):
            if self.grid[row][i] == 'x':
                i+=1
                continue
            if self.grid[row][i] == -1:
                i+=1
                continue
            if self.servers[self.grid[row][i]][2] == group:
                res.append(self.servers[self.grid[row][i]])
                i+= self.servers[self.grid[row][i]][0]

        return res

    def getGaranteedCapacity(self, groupIndex):
        res = 0
        values = []
        servers = []
        servers.append(serversInGroup(groupIndex))#servers[i] = servers in the group i
        totcap = sum(map(lambda x: x[1], servers))

        return totcap - max(sum(map(lambda x : x[1], self.getServIngroupInRow())))

    def getScore(self):
        return min(map(self.getGaranteedCapacity, range(self.groupsNumber)))



if __name__ == "__main__":
    Solver("dc.in")
