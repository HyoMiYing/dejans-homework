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
        # This example is taken directly from
        # the task instructions
        solution = v_pot('>69 ^69 <69')
        self.assertEqual(solution, [('>', 100), ('^', 42), ('<', 13)])

if __name__ == '__main__':
    unittest.main()