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
            fredkin_condition = set("0123456789+-").intersection(set(line))


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
        self.alive = False

class ConwayCell(AbstractCell):
    def __init__(self, x, y):
        AbstractCell.__init__(self, x, y)
        self.t = "c"


    def __repr__(self):
        if self.alive :
            return "*"
        return "."


class FredkinCell(AbstractCell):
    def __init__(self, x, y):
        AbstractCell.__init__(self, x ,y)
        self.t = "f"
        self.age = 0

    def __repr__(self):
        if self.alive :
            if self.age < 10:
                return str(self.age)
            return "+"
        return "-"


class Life:
    def __init__(self,initial_state, default):
        _, x, y = initial_state.pop()
        self.x = x
        self.y = y
        self.gen = 0
        self.pop = len(initial_state)
        self.d = default
        self.primary = self.Make_Grid("primary", default)
        self.secondary = self.Make_Grid("secondary",default)

        for t,x,y in initial_state:
            self.Add_Cell(t, x, y)

    def __repr__(self):
        stdout.write("Generation = " + str(self.gen) + "," + " Population = " + str(self.pop) + "\n")
        for i in range(self.x):
            assert type(i) is int
            for j in range(self.y):
                tile = self.primary[i][j]
                stdout.write(str(tile))
            stdout.write("\n")
        return ""

    def Make_Grid(self, priority, default):
        grid = [[]] * self.x
        for i in range(self.x):
            if priority == "primary":
                grid[i] = [default] * self.y
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
            self.secondary = self.Make_Grid("secondary",self.d)
            self.Tally()
            for j in range(self.y):
                for i in range(self.x):
                    numeric = self.secondary[i][j]
                    living  = self.primary[i][j]


                    # Conway cells and "." strings
                    if type(self.primary[i][j]) is str and numeric == 3 : # dead -> alive
                        self.Add_Cell("c", i, j)
                        continue

                    elif type(self.primary[i][j]) is ConwayCell:    # alive -> alive
                        if numeric > 1 or numeric < 4 :
                            self.primary[i][j].alive = True

                        if numeric < 2 or numeric > 3 : # alive -> dead
                            self.primary[i][j] = "."


                    # Fredkin cells and "-" strings
                    elif self.primary[i][j] == "-" and numeric in [1,3]: # dead -> alive
                        self.Add_Cell("f", i, j)


                    elif type(self.primary[i][j]) is FredkinCell:
                        if self.primary[i][j].alive and numeric in [0,2,4]: # alive -> dead
                            self.primary[i][j] = "-"
                            continue
                        elif self.primary[i][j].alive and numeric in [1,3] and self.primary[i][j].age < 2: # alive += age
                            self.primary[i][j].age += 1

                        elif self.primary[i][j].age == 2: # fredkin -> conway
                            self.Add_Cell("c", i ,j)
                            continue

            # loop for population count
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