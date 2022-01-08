import os
import sys

sys.path.append('../')
sys.path.append('../queries_functions')

import unittest
import pathlib as pl
import queries_functions.extendedV2_queries as q
import initialisation as i
from arango import ArangoClient

import warnings


class TestAdditionalFunctions(unittest.TestCase):
    database = None

    @classmethod
    def setUpClass(cls):
        cls.database = i.database_start("testDB", "root", "Amyloids", "extendedV2")

    @classmethod
    def tearDownClass(cls):
        client = ArangoClient()
        sys_db = client.db("_system", username="root", password="Amyloids")
        sys_db.delete_database("testDB")

        files = os.listdir("../tests/test_json_data")
        for file in files:
            os.remove("../tests/test_json_data/" + file)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def test_filter_question_extendedV2(self):
        q.filter_questions_extendedV2(self.database, q1="Slower aggregation", q2="No", q3="No information", filename="test_filter_1",
                                      directory="../tests/test_json_data")
        path = pl.Path("../tests/test_json_data/test_filter_1.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.filter_questions_extendedV2(self.database, q1="Slower aggregation", q3="No information",
                                      filename="test_filter_2",
                                      directory="../tests/test_json_data")
        path = pl.Path("../tests/test_json_data/test_filter_2.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.filter_questions_extendedV2(self.database, filename="test_filter_3", directory="../tests/test_json_data")
        path = pl.Path("../tests/test_json_data/test_filter_3.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

    def test_contains_fragment(self):
        q.contains_fragment_extendedV2(self.database, "DAEFRHDSG", filename="test_contains_1",
                                       directory="../tests/test_json_data")
        path = pl.Path("../tests/test_json_data/test_contains_1.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

    def test_search_phrase(self):
        q.search_phrase_extendedV2(self.database, "pH", filename="test_phrase_1",
                                   directory="../tests/test_json_data")
        path = pl.Path("../tests/test_json_data/test_phrase_1.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))


if __name__ == '__main__':
    unittest.main()
