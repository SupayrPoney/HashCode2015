class Solver:
    def __init__(self, filename):
        self.parse(filename)

    def parse(self, filename):
        with open(filename, "r") as f:
            self.r, self.s, self.u, self.p, self.m = map(int, f.readline().strip().split())

            self.grid = [[0 for i in range(self.s)] for j in range(self.r)]

            # unavailable spots
            for i in range(self.u):
                r, s = map(int, f.readline().strip().split())
                self.grid[r][s] = "X"

            # all servers
            self.servers = []
            while True:
                line = f.readline()
                if not line : break
                s, c = map(int, line.strip().split())
                self.servers.append((s,c))

if __name__ == "__main__":
    Solver("dc.in")
