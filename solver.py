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
            if server[0] > size: continue
            if server[3] == True : continue
            return i-1
        return -1



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
            else:
                i+=1

        return res

    def getGaranteedCapacity(self, groupIndex):
        servers = self.serversInGroup(groupIndex)#servers[i] = servers in the group i
        totcap = sum(map(lambda x: x[1], servers))

        maxi = 0
        for row in range(self.rangesNumber):
            cap = sum(map(lambda x: x[1], self.getServIngroupInRow(groupIndex,row)))
            if cap>maxi :
                maxi = cap


        return totcap - maxi

    def getScore(self):
        return min(map(self.getGaranteedCapacity, range(self.groupsNumber)))

    def saveOutput(self):
        with open(filename, "w") as f:
            i=0
            j=0
            while i < len(self.grid):
                while j < len(self.grid[i]):
                    if self.grid[i][j] != -1 and self.grid[i][j] != 'x':
                        f.write()


    def __repr__(self):
        res = ""
        for i in range(self.rangesNumber):
            for j in range(self.slotsPerRange):
                res += str(self.grid[i][j]) + " "
            res += "\n"
        return res

    def maxHoleSize(self):
        longest, now = 0, 0
        for line in self.grid:
            now = 0
            for serv in line:
                if serv == -1:
                    now += 1
                else:
                    if now > longest:
                        longest = now
                    now = 0
        return max(longest, now)


if __name__ == "__main__":
    s = Solver("dc.in")
    print s