import os
import sys
import warnings

sys.path.append('../')
sys.path.append('../initialisation_functions')
sys.path.append('../initialisation_functions/data')

import unittest
import pathlib as pl
import initialisation_functions.extended_json as j


class TestAdditionalFunctions(unittest.TestCase):

    def tearDown(self):
        files = os.listdir("../tests/test_json_data")
        for file in files:
            os.remove("../tests/test_json_data/" + file)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def test_questionnaire_simple(self):
        j.questionnaire_extended("../initialisation_functions/data/questionnaire.xlsx",
                                 output_dir="../tests/test_json_data/", join=False)
        path = pl.Path("../tests/test_json_data/amyloidsE.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

    def test_experiments_simple(self):
        j.experiments_extended("../initialisation_functions/data/experiments.xlsx",
                               output_dir="../tests/test_json_data/", join=False)
        path = pl.Path("../tests/test_json_data/amyloidsE.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))


if __name__ == '__main__':
    unittest.main()
