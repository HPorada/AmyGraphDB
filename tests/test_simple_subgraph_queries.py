import os
import sys

sys.path.append('../')
sys.path.append('../queries_functions')

import unittest
import pathlib as pl
import queries_functions.simple_subgraph_queries as q
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

        files = os.listdir("../tests/test_json_data")
        for file in files:
            os.remove("../tests/test_json_data/" + file)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def test_full_graph_simple(self):
        q.full_graph_simple(self.database, filename="test_full_1", directory="../tests/test_json_data")
        path = pl.Path("../tests/test_json_data/test_full_1.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

    def test_subgraph_from_interactions_simple(self):
        q.subgraph_from_interactions_simple(self.database, "Slower aggregation", "No", "No information", "test_int_1",
                                            "../tests/test_json_data")
        path = pl.Path("../tests/test_json_data/test_int_1.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.subgraph_from_interactions_simple(self.database, q1="Slower aggregation", q3="No information",
                                            filename="test_int_2",
                                            directory="../tests/test_json_data")
        path = pl.Path("../tests/test_json_data/test_int_2.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.subgraph_from_interactions_simple(self.database, filename="test_int_3", directory="../tests/test_json_data")
        path = pl.Path("../tests/test_json_data/test_int_3.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

    def test_subgraph_from_sequence_simple(self):
        q.subgraph_from_sequence_simple(self.database, sequence="MEFVAKLFKFFKDLLGKFLGNN", filename="test_seq_1",
                                        directory="../tests/test_json_data")
        path = pl.Path("../tests/test_json_data/test_seq_1.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.subgraph_from_sequence_simple(self.database, name="PPT_23", filename="test_seq_2",
                                        directory="../tests/test_json_data")
        path = pl.Path("../tests/test_json_data/test_seq_2.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

        q.subgraph_from_sequence_simple(self.database, filename="test_seq_3",
                                        directory="../tests/test_json_data")
        path = pl.Path("../tests/test_json_data/test_seq_3.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

    def test_subgraph_from_amyloid_simple(self):
        q.subgraph_from_amyloid_simple(self.database, amyloid="Sup35", filename="test_amy_1",
                                       directory="../tests/test_json_data")
        path = pl.Path("../tests/test_json_data/test_amy_1.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

    def test_subgraph_from_organism_simple(self):
        q.subgraph_from_organism_simple(self.database, organism="Coleophoma_crateriformis", filename="test_org_1",
                                        directory="../tests/test_json_data")
        path = pl.Path("../tests/test_json_data/test_org_1.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))


if __name__ == '__main__':
    unittest.main()
