import os
import sys

sys.path.append('../')
sys.path.append('../initialisation_functions')

import unittest
import pathlib as pl
import initialisation_functions.additional_functions as add


class TestAdditionalFunctions(unittest.TestCase):

    def tearDown(self):
        files = os.listdir("../tests/test_json_data")
        for file in files:
            os.remove("../tests/test_json_data/" + file)

    # def test_open_excel_file(self):
    #     pass

    def test_check_for_greek(self):
        self.assertEqual(add.check_for_greek('α-synuclein'), 'alpha-synuclein')
        self.assertEqual(add.check_for_greek('Γ'), 'gamma')
        self.assertEqual(add.check_for_greek('amyloid β'), 'amyloid beta')

    def test_create_json(self):
        col = [{"test": "test_value"}, {"test2": "test_value2"}]
        add.create_json("../tests/test_json_data/test_file.json", col)
        path = pl.Path("../tests/test_json_data/test_file.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

    def test_join_json(self):
        col = [{"test3": "test_value3"}, {"test4": "test_value4"}]
        add.join_json("../tests/test_json_data/test_file.json", col)
        path = pl.Path("../tests/test_json_data/test_file.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

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
