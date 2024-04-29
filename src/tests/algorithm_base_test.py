import os
import unittest
from services.map_file_translator import map_file_translator
from algorithms.fringe_search import fringe_search
from algorithms.a_star import a_star


class TestAlgorithmBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '''
        These tests are run on moving ai labs map AR0022SR.map. 
        The inputs_outputs list contains data parsed from the .map.scene file in a format ((start tuple), (goal tuple), (cost)).
        The list is 150 cases long. Witht the num_of_test_cases variable you can tune how meny run.
        150 cases might be a litle demanding for your machine.

        These test are designed to give a reasonable cerainty that the algorithms are running correctly.
        '''
        num_of_test_cases = 1

        super(TestAlgorithmBase, cls).setUpClass()
        inputs_outputs = [((6, 40), (8, 43), 3.82842712), ((55, 29), (53, 30), 2.41421356), ((57, 30), (56, 32), 2.41421356), ((29, 43), (27, 44), 3.0), ((36, 23), (33, 22), 3.41421356), ((12, 41), (12, 44), 3.0), ((42, 22), (41, 22), 1.0), ((21, 54), (24, 53), 3.41421356), ((32, 54), (33, 53), 1.41421356), ((23, 44), (21, 42), 3.41421356), ((43, 20), (43, 27), 7.0), ((39, 50), (37, 44), 6.82842712), ((12, 48), (9, 43), 6.24264069), ((17, 36), (20, 31), 6.82842712), ((33, 36), (28, 31), 7.07106781), ((31, 47), (32, 43), 4.41421356), ((37, 26), (35, 31), 5.82842712), ((43, 34), (50, 34), 7.0), ((23, 51), (17, 52), 6.41421356), ((8, 44), (12, 40), 6.24264069), ((39, 23), (39, 33), 10.0), ((30, 51), (24, 55), 8.24264069), ((44, 34), (51, 37), 8.24264069), ((46, 36), (50, 27), 10.65685425), ((12, 45), (16, 37), 9.65685425), ((53, 38), (44, 38), 9.0), ((29, 16), (36, 25), 11.89949493), ((20, 42), (24, 32), 11.65685425), ((11, 48), (7, 40), 9.65685425), ((31, 15), (39, 16), 8.41421356), ((37, 17), (28, 22), 13.65685425), ((28, 50), (34, 39), 13.48528137), ((17, 49), (23, 38), 15.72792206), ((28, 49), (38, 49), 13.07106781), ((39, 14), (28, 18), 12.65685425), ((21, 51), (10, 44), 13.89949493), ((19, 37), (27, 45), 14.24264069), ((40, 22), (33, 35), 15.89949493), ((46, 27), (32, 28), 14.41421356), ((12, 47), (15, 36), 12.24264069), ((34, 41), (21, 50), 16.72792206), ((14, 42), (20, 56), 16.48528137), ((39, 31), (25, 21), 18.14213562), ((26, 48), (13, 38), 18.89949493), ((34, 29), (30, 47), 19.65685425), ((29, 50), (33, 33), 18.65685425), ((22, 39), (34, 40), 17.72792206), ((31, 41), (34, 55), 16.07106781), ((31, 23), (45, 28), 16.07106781), ((11, 44), (24, 58), 19.38477631), ((36, 47), (22, 39), 21.41421356), ((23, 38), (39, 41), 20.55634918), ((31, 14), (43, 18), 20.72792206), ((47, 20), (47, 42), 22.0), ((31, 32), (52, 32), 21.0), ((49, 28), (35, 37), 21.48528137), ((30, 17), (44, 32), 20.79898987), ((47, 32), (24, 33), 23.41421356), ((34, 13), (33, 31), 21.48528137), ((33, 19), (38, 39), 22.65685425), ((34, 58), (30, 36), 25.89949493), ((40, 34), (35, 18), 27.14213562), ((42, 28), (18, 35), 26.89949493), ((24, 58), (32, 35), 27.14213562), ((28, 21), (31, 45), 27.72792206), ((24, 46), (39, 31), 24.72792206), ((22, 55), (20, 32), 26.65685425), ((19, 52), (28, 32), 27.04163055), ((29, 31), (53, 35), 25.65685425), ((33, 35), (55, 35), 25.07106781), ((25, 38), (48, 23), 29.79898987), ((19, 40), (44, 27), 30.38477631), ((38, 49), (31, 23), 28.89949493), ((20, 29), (42, 21), 29.55634918), ((45, 23), (29, 44), 28.21320343), ((48, 40), (23, 30), 29.14213562), ((
            20, 32), (48, 32), 28.0), ((54, 28), (35, 40), 29.48528137), ((21, 38), (41, 51), 28.89949493), ((21, 30), (45, 24), 28.14213562), ((33, 57), (39, 26), 35.97056274), ((38, 48), (31, 17), 33.89949493), ((3, 41), (32, 36), 33.55634918), ((51, 24), (37, 45), 33.97056274), ((36, 28), (13, 51), 34.87005768), ((23, 61), (35, 33), 33.55634918), ((54, 38), (24, 31), 32.89949493), ((38, 11), (47, 30), 32.04163055), ((39, 13), (50, 30), 35.21320343), ((35, 13), (22, 34), 34.72792206), ((54, 30), (22, 40), 36.14213562), ((39, 12), (30, 43), 39.55634918), ((33, 15), (38, 48), 37.3137085), ((41, 16), (35, 43), 38.65685425), ((14, 43), (46, 34), 37.38477631), ((36, 19), (53, 37), 38.6984848), ((49, 31), (29, 52), 36.89949493), ((43, 39), (32, 56), 38.38477631), ((29, 49), (55, 33), 39.89949493), ((53, 30), (39, 47), 36.89949493), ((17, 38), (35, 15), 40.55634918), ((43, 36), (10, 46), 40.45584412), ((6, 39), (36, 24), 42.21320343), ((20, 51), (26, 21), 40.28427124), ((52, 28), (14, 39), 42.55634918), ((40, 24), (23, 60), 43.04163055), ((13, 35), (49, 40), 41.38477631), ((51, 32), (13, 42), 42.14213562), ((50, 32), (15, 49), 43.79898987), ((37, 20), (32, 46), 40.3137085), ((36, 15), (14, 41), 45.79898987), ((50, 39), (13, 47), 46.11269836), ((38, 15), (16, 38), 44.55634918), ((49, 36), (14, 51), 46.87005768), ((55, 36), (32, 53), 45.55634918), ((55, 34), (24, 54), 47.38477631), ((48, 37), (22, 59), 47.45584412), ((17, 51), (51, 33), 45.79898987), ((16, 52), (49, 35), 46.04163055), ((27, 47), (40, 17), 44.55634918), ((7, 43), (50, 39), 50.45584412), ((33, 16), (15, 53), 50.45584412), ((50, 38), (25, 60), 51.28427124), ((48, 34), (4, 41), 49.38477631), ((33, 53), (60, 32), 49.89949493), ((42, 15), (23, 44), 48.38477631), ((5, 38), (49, 32), 50.38477631), ((31, 52), (41, 15), 49.72792206), ((57, 33), (35, 55), 50.14213562), ((41, 51), (38, 11), 48.21320343), ((22, 59), (35, 11), 55.87005768), ((37, 10), (15, 51), 54.94112549), ((59, 31), (14, 49), 53.62741699), ((15, 50), (35, 10), 53.11269836), ((29, 62), (26, 20), 52.94112549), ((44, 21), (29, 62), 52.76955261), ((40, 18), (35, 56), 54.79898987), ((41, 15), (11, 44), 55.04163055), ((22, 52), (41, 16), 52.21320343), ((23, 59), (34, 14), 52.62741699), ((3, 40), (56, 33), 58.38477631), ((40, 13), (8, 44), 57.87005768), ((16, 49), (42, 15), 56.28427124), ((35, 18), (5, 39), 56.45584412), ((42, 16), (15, 50), 56.45584412), ((25, 60), (36, 19), 57.45584412), ((41, 17), (34, 58), 56.97056274), ((21, 59), (37, 15), 56.04163055), ((5, 40), (38, 15), 58.04163055), ((40, 14), (22, 56), 56.04163055)]

        cls.inputs_outputs = inputs_outputs[:num_of_test_cases]

        path = os.path.join(
            os.getcwd(), "src/map_generation/maps/AR0022SR.map")
        cls.map_path = path
        with open(cls.map_path, "r") as f:
            cls.map_data = f.read()

    def test_dijkstra_correct_path(self):
        for start, goal, cost in self.inputs_outputs:
            result = map_file_translator(
                start=start,
                goal=goal,
                grid=self.map_data,
                algorithm=a_star,
                heurestic=lambda x, y, z: 0)
            self.assertAlmostEqual(cost, result['cost'])

    def test_a_star_correct_path(self):
        for start, goal, cost in self.inputs_outputs:
            result = map_file_translator(
                start=start,
                goal=goal,
                grid=self.map_data,
                algorithm=a_star
            )
            self.assertAlmostEqual(cost, result['cost'])

    def test_fringe_search_correct_path(self):
        for start, goal, cost in self.inputs_outputs:
            result = map_file_translator(
                start=start,
                goal=goal,
                grid=self.map_data,
                algorithm=fringe_search
            )
            self.assertAlmostEqual(cost, result['cost'])