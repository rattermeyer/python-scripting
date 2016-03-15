import unittest
import list_intersection


class TestListIntersection(unittest.TestCase):
    def test_intersection(self):
        self.assertEqual("b", list_intersection.intersect("a,b,c", "b,d,e"))
        self.assertEqual("b",list_intersection.intersect("c,b,a", "b,d,e"))
        self.assertEqual("b,b", list_intersection.intersect("c,b,b", "b,b,e"))

    def test_emptyIntersection(self):
        self.assertEqual("", list_intersection.intersect("a,b,c", "d,e,f"))

    def test_emptyListA(self):
        self.assertEqual("", list_intersection.intersect("", "d,e,f"))
        self.assertEqual("d,e,f", list_intersection.intersect(None, "d,e,f"))

    def test_emptyListB(self):
        self.assertEqual("", list_intersection.intersect("d,e,f", ""))
        self.assertEqual("d,e,f", list_intersection.intersect("d,e,f", None))

    def test_empty(self):
        self.assertEqual(None, list_intersection.intersect(None, None))
