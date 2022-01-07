import sys
import unittest
import initialisation_functions.additional_functions as add

sys.path.append('../')
sys.path.append('../initialisation_functions')


class TestAdditionalFunctions(unittest.TestCase):

    # def test_open_excel_file(self):
    #     pass

    def test_check_for_greek(self):
        self.assertEqual(add.check_for_greek('α-synuclein'), 'alpha-synuclein')
        self.assertEqual(add.check_for_greek('Γ'), 'gamma')
        self.assertEqual(add.check_for_greek('amyloid β'), 'amyloid beta')

    # def test_create_json(self):
    #     pass

    # def test_join_json(self):
    #     pass

    def test_get_temp(self):
        self.assertEqual(add.get_temp('-10-15'), ['psychrophilic', 'mesophilic'])
        self.assertEqual(add.get_temp('5'), ['psychrophilic'])
        self.assertEqual(add.get_temp('15-25'), ['mesophilic'])
        self.assertEqual(add.get_temp('75-80'), ['thermophilic', 'hyperthermophilic'])
        self.assertEqual(add.get_temp('test'), [])

    def test_get_ph(self):
        self.assertEqual(add.get_ph('3-5'), ['acidophilic', 'neutrophilic'])
        self.assertEqual(add.get_ph('11-14'), ['alkaliphilic'])
        self.assertEqual(add.get_ph('test'), [])


if __name__ == '__main__':
    unittest.main()
