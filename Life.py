__author__ = 'El Dueno'


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
        pass




#------
# demo
#------

all_events = gather(stdin)

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




