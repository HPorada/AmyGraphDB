import os
import sys
import warnings

sys.path.append('../')
sys.path.append('../initialisation_functions')
sys.path.append('../initialisation_functions/data')

import unittest
import pathlib as pl
import initialisation as i
from arango import ArangoClient
from config.definitions import USERNAME, PASSWORD

import warnings


class TestAdditionalFunctions(unittest.TestCase):
    client = None
    db_sys = None

    @classmethod
    def setUpClass(cls):
        cls.client = ArangoClient(hosts='http://localhost:8529')
        cls.db_sys = cls.client.db('_system', username=USERNAME, password=PASSWORD)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    @classmethod
    def tearDownClass(cls):
        files = os.listdir("../tests/test_json_data")
        for file in files:
            os.remove("../tests/test_json_data/" + file)

    def tearDown(self):
        if self.db_sys.has_database("testDB"):
            self.db_sys.delete_database("testDB")

    def test_database_start(self):
        self.assertEqual(self.db_sys.has_database("testDB"), False)
        i.database_start("testDB", USERNAME, PASSWORD, "simple")
        self.assertEqual(self.db_sys.has_database("testDB"), True)

    def test_create_json_files(self):
        i.create_json_files("simple", "../initialisation_functions/data/questionnaire.xlsx",
                            "../initialisation_functions/data/experiments.xlsx",
                            "../tests/test_json_data")
        path = pl.Path("../tests/test_json_data/amyloids.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        i.create_json_files("extended", "../initialisation_functions/data/questionnaire.xlsx",
                            "../initialisation_functions/data/experiments.xlsx",
                            "../tests/test_json_data")
        path = pl.Path("../tests/test_json_data/amyloidsE.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        i.create_json_files("extendedV2", "../initialisation_functions/data/questionnaire.xlsx",
                            "../initialisation_functions/data/experiments.xlsx",
                            "../tests/test_json_data")
        path = pl.Path("../tests/test_json_data/amyloidsE.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        with self.assertRaises(ValueError):
            i.create_json_files("test", "../initialisation_functions/data/questionnaire.xlsx",
                                "../initialisation_functions/data/experiments.xlsx",
                                "../tests/test_json_data")

    def test_connect_to_database(self):
        i.connect_to_database("testDB", USERNAME, PASSWORD)
        self.assertEqual(self.db_sys.has_database("testDB"), True)

    def test_import_collections(self):
        self.db_sys.create_database("testDB")
        db = self.client.db("testDB", USERNAME, PASSWORD)
        i.create_json_files("simple", "../initialisation_functions/data/questionnaire.xlsx",
                            "../initialisation_functions/data/experiments.xlsx",
                            "../tests/test_json_data")
        i.import_collections(db, "../tests/test_json_data")

        self.assertEqual(db.has_collection("amyloids"), True)

    def test_create_graph(self):
        self.db_sys.create_database("testDB")
        db = self.client.db("testDB", USERNAME, PASSWORD)
        i.create_json_files("simple", "../initialisation_functions/data/questionnaire.xlsx",
                            "../initialisation_functions/data/experiments.xlsx",
                            "../tests/test_json_data")
        i.import_collections(db, "../tests/test_json_data")

        i.create_graph(db, "simple")

        self.assertEqual(db.has_graph("Simple"), True)

    def test_create_view(self):
        self.db_sys.create_database("testDB")
        db = self.client.db("testDB", USERNAME, PASSWORD)
        i.create_json_files("simple", "../initialisation_functions/data/questionnaire.xlsx",
                            "../initialisation_functions/data/experiments.xlsx",
                            "../tests/test_json_data")
        i.import_collections(db, "../tests/test_json_data")

        i.create_view(db, "simple")

        self.assertEqual(db.view("simpleView") is not None, True)

    def test_delete_database(self):
        i.connect_to_database("testDB", USERNAME, PASSWORD)
        self.assertEqual(self.db_sys.has_database("testDB"), True)

        i.delete_database("testDB", USERNAME, PASSWORD)
        self.assertEqual(self.db_sys.has_database("testDB"), False)


if __name__ == '__main__':
    unittest.main()
