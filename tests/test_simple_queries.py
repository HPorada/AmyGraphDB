import sys

sys.path.append('../')
sys.path.append('../queries_functions')

import unittest
import pathlib as pl
import queries_functions.simple_queries as sq
import initialisation as i
from arango import ArangoClient

import warnings


class TestAdditionalFunctions(unittest.TestCase):
    database = None

    @classmethod
    def setUpClass(cls):
        cls.database = i.database_start("testDB", "root", "Amyloids", "simple")

    @classmethod
    def tearDownClass(cls):
        client = ArangoClient()
        sys_db = client.db("_system", username="root", password="Amyloids")
        sys_db.delete_database("testDB")
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def test_filter_question_simple(self):
        sq.filter_questions_simple(self.database, "Slower aggregation", "No", "No information", "test_filter",
                                   "../tests/test_json_data")
        path = pl.Path("../tests/test_json_data/test_filter.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        sq.filter_questions_simple(self.database, q1="Slower aggregation", q3="No information", filename="test_filter",
                                   directory="../tests/test_json_data")
        path = pl.Path("../tests/test_json_data/test_filter.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        sq.filter_questions_simple(self.database, filename="test_filter", directory="../tests/test_json_data")
        path = pl.Path("../tests/test_json_data/test_filter.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))


if __name__ == '__main__':
    unittest.main()
