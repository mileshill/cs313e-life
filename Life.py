__author__ = 'El Dueno'

from collections import defaultdict
from sys import stdin,stdout

def reader(r):
    s = r.readline()
    return s



def gather(r):
    """ Returns a list of ordered pairs with conway/fredkin indicator. List of pairs represents a gameboard """
    event = list()
    while True:
        try:
            row =  int(reader(r))  # read the first row
            column = int(reader(r)) # read the column
        except ValueError:
            break #breaks at EOF

        alive = list()
        for row_num in range(row + 1): # collects blank at end
            line =  reader(r).strip()
            conway_condition = "*" in list(line)
            fredkin_condition = set("0123456789+").intersection(set(line))


            if conway_condition or fredkin_condition :
                l = [["c",row_num, i] for i,j in enumerate( list(line)) if j == "*"]  # list of indicies
                k = [["f",row_num, i] for i,j in enumerate(list(line)) if  fredkin_condition.intersection(j) ]

                if l: alive.extend(l)
                if k: alive.extend(k)
        alive.extend([["dim",row,column]])
        event.extend([alive])

    return event


class AbstractCell:
    def __init__(self, x ,y):
        self.x = x
        self.y = y


class ConwayCell(AbstractCell):
    def __init__(self, x, y):
        AbstractCell.__init__(self, x, y)
        self.t = "c"
        self.alive = False

    def __repr__(self):
        if self.alive :
            return "*"
        return "."

class FredkinCell(AbstractCell):
    def __init__(self, x, y):
        AbstractCell.__init__(self, x ,y)
        self.t = "f"
        self.alive = False
        self.age = 0

    def __repr__(self):
        if self.alive :
            if self.age < 10:
                return str(self.age)
            return "+"
        return "-"


class Life:
    def __init__(self,initial_state):

        _, x, y = initial_state.pop()
        self.x = x
        self.y = y
        self.gen = 0
        self.pop = len(initial_state)
        self.primary = self.Make_Grid("primary")
        self.secondary = self.Make_Grid("secondary")

        for t,x,y in initial_state:
            self.Add_Cell(t, x, y)



    def __repr__(self):
        stdout.write("Generation = " + str(self.gen) + "," + " Population = " + str(self.pop) + "\n")
        for i in range(self.x):
            for j in range(self.y):
                tile = self.primary[i][j]
                stdout.write(str(tile))
            stdout.write("\n")
        return ""

    def Make_Grid(self, priority):
        grid = [[]] * self.x
        for i in range(self.x):
            if priority == "primary":
                grid[i] = ["."] * self.y
                continue

            grid[i] = [0] * self.y

        return grid



    def Add_Cell(self, t, x ,y):
        if t == "c":
            cell = ConwayCell(x,y)
        else:
            cell = FredkinCell(x,y)

        cell.alive = True
        self.primary[x][y] = cell

    def Tally(self):
        loc = defaultdict(list)
        for i in range(self.x):
            for j in range(self.y):
                tile = self.primary[i][j]
                if type(tile) is ConwayCell or type(tile) is FredkinCell and tile.alive:
                    loc[tile.t] += [[tile.x,tile.y]]


        if "c" in loc:
            for item in loc["c"]:
                x, y = item
                try:
                    self.secondary[x][y + 1] += 1 # north
                except IndexError:
                    pass
                try:
                    self.secondary[x + 1][y + 1] += 1 # north east
                except IndexError:
                    pass
                try:
                    self.secondary[x + 1][y] += 1 # east
                except IndexError:
                    pass
                try:
                    self.secondary[x + 1][y - 1] += 1 # south east
                except IndexError:
                    pass
                try:
                    self.secondary[x][y - 1] += 1 # south
                except IndexError:
                    pass
                try:
                    self.secondary[x - 1][y - 1] += 1 # south west
                except IndexError:
                    pass
                try:
                    self.secondary[x - 1][y] += 1 # west
                except IndexError:
                    pass
                try:
                    self.secondary[x - 1][y + 1] += 1 # north west
                except IndexError:
                    pass


        if "f" in loc:
            for item in loc["f"]:
                x, y = item
                try:
                    self.secondary[x][y + 1] += 1 # north
                except IndexError:
                    pass
                try:
                    self.secondary[x + 1][y] += 1 # east
                except IndexError:
                    pass
                try:
                    self.secondary[x][y - 1] += 1 # south
                except IndexError:
                    pass
                try:
                    self.secondary[x - 1][y] += 1 # west
                except IndexError:
                    pass

    def Evolve(self, steps, print_list):
        stdout.write(self.__repr__())

        for turn in range(1, steps + 1):
            self.pop = 0
            self.gen = turn
            self.secondary = self.Make_Grid("secondary")
            self.Tally()
            for j in range(self.y):
                for i in range(self.x):
                    numeric = self.secondary[i][j]
                    living  = self.primary[i][j]

                    if type(self.primary[i][j]) is str and numeric == 3 :
                        self.Add_Cell("c", i, j)

                    elif type(self.primary[i][j]) is ConwayCell:
                        if numeric > 1 or numeric < 4 :
                            self.primary[i][j].alive = True


                        if numeric < 2 or numeric > 3 :
                            self.primary[i][j] = "."

            current = 0
            for i in range(self.x):
                for j in range(self.y):
                    if type(self.primary[i][j]) is ConwayCell or type(self.primary[i][j]) is FredkinCell:
                        if self.primary[i][j].alive :
                            current += 1

            self.pop = current


            if turn in print_list:
                stdout.write(self.__repr__())
                stdout.write("\n")


        stdout.write("\n")



#------
# demo
#------
"""
all_events = gather(stdin)

single_event = all_events[0]

l = Life(single_event)
l.Evolve(12)


tester = [['c',3,2],['c',3,3],['c',3,4],['dim',6,7]]
m = Life(tester)
m.Evolve(5)



stdout.write("Initial Conditions: ie, all living cells in grid\n")
for event in all_events:
    stdout.write( str(event) + "\n")


n = ConwayCell(1,1)
stdout.write("Dead Conway --> " + str(n) + '\n')
n.alive = True
stdout.write("Alive Conway --> " + str(n) + '\n')

m = FredkinCell(1,1)
stdout.write("Dead Fredkin --> " + str(m) + '\n' )
m.alive = True
stdout.write("Alive Fredkin --> " + str(m) + '\n')
m.age = 8
stdout.write("Fredkin: age < 10 : " + str(m) + "\n")
m.age = 10
stdout.write("Fredkin: age >= 10 : " + str(m) + '\n')
"""





