import unittest
from dejanova_naloga import v_pot, odsek, tocke, presecisce

class RundownTest(unittest.TestCase):
    # Name 'Rundown Test' is because test runs down the
    # script and checks if every function is working as
    # it should

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_1st_task_happy_path(self):
        # These examples are taken directly from
        # the task instructions
        solution = v_pot('>100 ^42 <13')
        self.assertEqual(solution, [('>', 100), ('^', 42), ('<', 13)])

    def test_2nd_task_happy_path(self):
        solution = odsek(2, 5, '^', 3)
        self.assertEqual(solution, [(2, 5), (2, 6), (2, 7), (2, 8)])
        

    def test_3nd_task_happy_path(self):
        solution = tocke([('>', 3), ('v', 2), ('>', 2)])
        self.assertEqual(solution, [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (3, -1),
            (3, -2),
            (4, -2),
            (5, -2),
            ])
        

    def test_4nd_task_happy_path(self):
        # This task does not have an example in instructions
        solution = presecisce('^2 >6 ^6 <1', '>1 ^3 >6')
        self.assertEqual(solution, [(0, 0), (1, 2), (6, 3)])

if __name__ == '__main__':
    unittest.main()