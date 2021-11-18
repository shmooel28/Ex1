import unittest

from Buildings import Buildings
from main import read_from_csv


class MyTestCase(unittest.TestCase):
    def test_building(self):
        building = Buildings("Ex1_input/Ex1_Buildings/B1.json")
        self.assertEqual(building.minFloor, -2)

    def test_elevator(self):
        building = Buildings("Ex1_input/Ex1_Buildings/B1.json")
        self.assertEqual(building.elevators[0].id, 0)

    def test_update(self):
        buildings = Buildings("Ex1_input/Ex1_Buildings/B1.json")
        buildings.update_elevator(0)
        self.assertEqual(buildings.elevators[0].pos, 0)


if __name__ == '__main__':
    unittest.main()
