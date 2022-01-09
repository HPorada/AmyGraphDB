import os
import sys

sys.path.append('../')
# sys.path.append('../queries_functions')

import unittest
import pathlib as pl
import queries as q
import initialisation as i
from arango import ArangoClient

import warnings


class TestAdditionalFunctions(unittest.TestCase):
    database = None

    @classmethod
    def setUpClass(cls):
        cls.databaseS = i.database_start("testDB_S", "root", "Amyloids", "simple")
        cls.databaseE = i.database_start("testDB_E", "root", "Amyloids", "extended")
        cls.databaseE2 = i.database_start("testDB_E2", "root", "Amyloids", "extendedV2")

    @classmethod
    def tearDownClass(cls):
        client = ArangoClient()
        sys_db = client.db("_system", username="root", password="Amyloids")
        sys_db.delete_database("testDB_S")
        sys_db.delete_database("testDB_E")
        sys_db.delete_database("testDB_E2")

        files = os.listdir("../tests/test_json_data")
        for file in files:
            os.remove("../tests/test_json_data/" + file)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def test_custom_query(self):
        query = """for i in interactions
            filter i.question_1 == "Slower aggregation"
            filter i.question_3 == "Yes"
            return i"""
        q.custom_query(self.databaseS, query, "test_custom", "tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_custom.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

    def test_full_graph(self):
        q.full_graph("simple", self.databaseS, filename="test_full_1", directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_full_1.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.full_graph("extended", self.databaseE, filename="test_full_2", directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_full_2.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.full_graph("extendedV2", self.databaseE2, filename="test_full_3", directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_full_3.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        with self.assertRaises(ValueError):
            q.full_graph("test", self.databaseS, filename="test_full_4", directory="tests\\test_json_data")

    def test_filter_questions(self):
        q.filter_questions("simple", self.databaseS, "Slower aggregation", "No", "No information", "test_filter_1",
                           "tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_filter_1.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.filter_questions("extended", self.databaseE, "Slower aggregation", "No", "No information", "test_filter_2",
                           "tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_filter_2.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.filter_questions("extendedV2", self.databaseE2, "Slower aggregation", "No", "No information", "test_filter_3",
                           "tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_filter_3.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        with self.assertRaises(ValueError):
            q.filter_questions("test", self.databaseS, "Slower aggregation", "No", "No information", "test_filter_4",
                               "tests\\test_json_data")

    def test_contains_fragment(self):
        q.contains_fragment("simple", self.databaseS, "DAEFRHDSG", filename="test_contains_1",
                            directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_contains_1.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.contains_fragment("extended", self.databaseE, "DAEFRHDSG", filename="test_contains_2",
                            directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_contains_2.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.contains_fragment("extendedV2", self.databaseE2, "DAEFRHDSG", filename="test_contains_3",
                            directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_contains_3.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        with self.assertRaises(ValueError):
            q.contains_fragment("test", self.databaseS, "DAEFRHDSG", filename="test_contains_4",
                                directory="tests\\test_json_data")

    def test_search_phrase(self):
        q.search_phrase("simple", self.databaseS, "pH", filename="test_phrase_1",
                        directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_phrase_1.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.search_phrase("extended", self.databaseE, "pH", filename="test_phrase_2",
                        directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_phrase_2.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.search_phrase("extendedV2", self.databaseE2, "pH", filename="test_phrase_3",
                        directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_phrase_3.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        with self.assertRaises(ValueError):
            q.search_phrase("test", self.databaseS, "pH", filename="test_phrase_4",
                            directory="tests\\test_json_data")

    def test_subgraph_from_interactions(self):
        q.subgraph_from_interactions("simple", self.databaseS, "Slower aggregation", "No", "No information",
                                     filename="test_int_1", directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_int_1.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.subgraph_from_interactions("extended", self.databaseE, "Slower aggregation", "No", "No information",
                                     filename="test_int_2", directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_int_2.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.subgraph_from_interactions("extendedV2", self.databaseE2, "Slower aggregation", "No", "No information",
                                     filename="test_int_3", directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_int_3.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        with self.assertRaises(ValueError):
            q.subgraph_from_interactions("test", self.databaseS, "Slower aggregation", "No", "No information",
                                         filename="test_int_4", directory="tests\\test_json_data")

    def test_subgraph_from_sequence(self):
        q.subgraph_from_sequence("simple", self.databaseS, sequence="MEFVAKLFKFFKDLLGKFLGNN", filename="test_seq_1",
                                 directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_seq_1.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.subgraph_from_sequence("extended", self.databaseE, sequence="MEFVAKLFKFFKDLLGKFLGNN", filename="test_seq_2",
                                 directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_seq_2.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.subgraph_from_sequence("extendedV2", self.databaseE2, sequence="MEFVAKLFKFFKDLLGKFLGNN",
                                 filename="test_seq_3",
                                 directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_seq_3.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        with self.assertRaises(ValueError):
            q.subgraph_from_sequence("test", self.databaseS, sequence="MEFVAKLFKFFKDLLGKFLGNN", filename="test_seq_4",
                                     directory="tests\\test_json_data")

    def test_subgraph_from_amyloid(self):
        q.subgraph_from_amyloid("simple", self.databaseS, amyloid="Sup35", filename="test_amy_1",
                                directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_amy_1.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.subgraph_from_amyloid("extended", self.databaseE, amyloid="Sup35", filename="test_amy_2",
                                directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_amy_2.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.subgraph_from_amyloid("extendedV2", self.databaseE2, amyloid="Sup35", filename="test_amy_3",
                                directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_amy_3.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        with self.assertRaises(ValueError):
            q.subgraph_from_amyloid("test", self.databaseS, amyloid="Sup35", filename="test_amy_1",
                                    directory="tests\\test_json_data")

    def test_subgraph_from_organism(self):
        q.subgraph_from_organism("simple", self.databaseS, organism="Coleophoma_crateriformis", filename="test_org_1",
                                 directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_org_1.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.subgraph_from_organism("extended", self.databaseE, organism="Coleophoma_crateriformis", filename="test_org_2",
                                 directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_org_2.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.subgraph_from_organism("extendedV2", self.databaseE2, organism="Coleophoma_crateriformis",
                                 filename="test_org_3",
                                 directory="tests\\test_json_data")
        path = pl.Path("../tests/test_json_data/test_org_3.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        with self.assertRaises(ValueError):
            q.subgraph_from_organism("test", self.databaseS, organism="Coleophoma_crateriformis",
                                     filename="test_org_1",
                                     directory="tests\\test_json_data")


if __name__ == '__main__':
    unittest.main()
