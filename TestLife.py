__author__ = 'El Dueno'

from Life import *
from unittest import TestCase,main
from io import StringIO
class TestLife(TestCase):

    #------
    # reader
    #------
    def test_reader(self):
        j = StringIO("test")
        k = reader(j)
        self.assertEqual(k,"test")

    #--------
    # gather
    #--------
    def test_gather_1(self):
        j = StringIO("1\n13\n....*****....")
        k = gather(j)
        self.assertIsInstance(k,list)

    def test_gather_2(self):
        j = StringIO("1\n13\n....*****....")
        k = gather(j)
        _,x,y = k[0][-1]
        self.assertEqual(x,1)
        self.assertEqual(y,13)

    def test_gather_3(self):
        j = StringIO("1\n13\n....*****....")
        k = gather(j)
        t = k[0][0][0]
        self.assertTrue(t == "c")

    def test_gather_4(self):
        j = StringIO("1\n13\n....00000....")
        k = gather(j)
        t = k[0][0][0]
        self.assertTrue(t == "f")

    def test_gather_5(self):
        j = StringIO("1\n13\n....00000....")
        k = gather(j)
        t = k[0][:-1]
        self.assertEqual(t,[["f",0,4],["f",0,5],["f",0,6],["f",0,7],["f",0,8]])

    #------------
    # AbstractCell
    #------------
    def test_AbstractCell(self):
        j = AbstractCell(1,1)
        self.assertEqual(1,j.x)

    def test_AbstractCell_2(self):
        j = AbstractCell(1,1)
        self.assertEqual(1,j.y)

    #-------------
    # ConwayCell
    #-------------
    def test_ConwayCell(self):
        j = ConwayCell(1,1)
        self.assertEqual(1,j.x)

    def test_ConwayCell_2(self):
        j = ConwayCell(1,1)
        self.assertEqual(1,j.y)

    def test_ConwayCell_3(self):
        j = ConwayCell(1,1)
        self.assertEqual("c",j.t)

    def test_ConwayCell_4(self):
        j = ConwayCell(1,1)
        self.assertTrue(j.alive is False)

    def test_ConwayCell_5(self):
        j = ConwayCell(1,1)
        self.assertEqual(".", j.__repr__())
        j.alive = True
        self.assertEqual("*", j.__repr__())

    #------------------------
    # FredkinCell
    #-------------------------
    def test_FredkinCell(self):
        j = FredkinCell(1,1)
        self.assertEqual(1,j.x)

    def test_FredkinCell_2(self):
        j = FredkinCell(1,1)
        self.assertEqual(1,j.y)

    def test_FredkinCell_3(self):
        j = FredkinCell(1,1)
        self.assertEqual("f",j.t)

    def test_FredkinCell_4(self):
        j = FredkinCell(1,1)
        self.assertTrue(j.alive is False)

    def test_FredkinCell_5(self):
        j = FredkinCell(1,1)
        self.assertEqual("-", j.__repr__())
        j.alive = True
        self.assertEqual("0", j.__repr__())

    def test_FredkinCell_6(self):
        j = FredkinCell(1,1)
        j.age = 11
        j.alive = True
        self.assertEqual("+", j.__repr__())



    #-----------------
    # Life
    #----------------
    def test_Life(self):
        initial = [['c', 8, 4], ['c', 8, 5], ['c', 8, 6], ['c', 8, 7], ['c', 8, 8], ['c', 9, 7], ['c', 10, 6], ['c', 11, 5], ['c', 12, 4], ['c', 12, 5], ['c', 12, 6], ['c', 12, 7], ['c', 12, 8], ['dim', 21, 13]]
        j = Life(initial)
        self.assertEqual(j.x, 21)
        self.assertEqual(j.y, 13)
        self.assertEqual(j.gen, 0)
        self.assertEqual(j.pop, 13)
        self.assertIsInstance(j.primary, list)
        self.assertIsInstance(j.secondary, list)
        for item in initial:
            _, x, y = item
            self.assertIsInstance(j.primary[x][y], ConwayCell)

    #Make_Grid()
    def test_life_2(self):
        initial = [['c', 8, 4], ['c', 8, 5], ['c', 8, 6], ['c', 8, 7], ['c', 8, 8], ['c', 9, 7], ['c', 10, 6], ['c', 11, 5], ['c', 12, 4], ['c', 12, 5], ['c', 12, 6], ['c', 12, 7], ['c', 12, 8], ['dim', 21, 13]]
        j = Life(initial)
        self.assertEqual(21,len(j.primary))
        self.assertEqual(13, len(j.primary[0]))
        self.assertEqual(21,len(j.secondary))
        self.assertEqual(13, len(j.secondary[0]))

        for cell in j.primary[0]:
            self.assertIsInstance(cell,str)
            self.assertEqual(cell,".")

    #Add cell
    def test_life_3(self):
        initial = [['c', 8, 4], ['c', 8, 5], ['c', 8, 6], ['c', 8, 7], ['c', 8, 8], ['c', 9, 7], ['c', 10, 6], ['c', 11, 5], ['c', 12, 4], ['c', 12, 5], ['c', 12, 6], ['c', 12, 7], ['c', 12, 8], ['dim', 21, 13]]
        j = Life(initial)
        self.assertEqual(j.primary[0][0],".")
        self.assertEqual(j.primary[0][1],".")
        j.Add_Cell("c",0,0)
        j.Add_Cell("f",0,1)

        self.assertIsInstance(j.primary[0][0], ConwayCell)
        self.assertEqual(j.primary[0][0].__repr__(), "*")
        self.assertTrue(j.primary[0][0].alive)

        self.assertIsInstance(j.primary[0][1], FredkinCell)
        self.assertEqual(j.primary[0][1].__repr__(),"0")
        self.assertTrue(j.primary[0][1].alive)

    #Tally()
    def test_life_4(self):
        initial = [['c',1,1],['dim',3,3]]
        j = Life(initial)

        for row in j.secondary:
            for cell in row:
                self.assertEqual(cell,0)

        j.Tally()
        self.assertEqual(j.secondary[0],[1,1,1])
        self.assertEqual(j.secondary[1],[1,0,1])
        self.assertEqual(j.secondary[2],[1,1,1])

    #Tally()
    def test_life_5(self):
        initial = [['f',1,1],['dim',3,3]]
        j = Life(initial)

        for row in j.secondary:
            for cell in row:
                self.assertEqual(cell,0)

        j.Tally()
        self.assertEqual(j.secondary[0],[0,1,0])
        self.assertEqual(j.secondary[1],[1,0,1])
        self.assertEqual(j.secondary[2],[0,1,0])

    #Life.Evolve()

main()