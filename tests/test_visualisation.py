import os
import sys
import warnings

sys.path.append('../')
sys.path.append('../initialisation_functions')
sys.path.append('../initialisation_functions/data')

import unittest
import pathlib as pl
import initialisation as i
import queries as q
import visualisation as v
from arango import ArangoClient
from config.definitions import USERNAME, PASSWORD

import warnings


class TestAdditionalFunctions(unittest.TestCase):
    database = None

    @classmethod
    def setUpClass(cls):
        cls.database = i.database_start("testDB", USERNAME, PASSWORD, "extended")
        query = """for i in interactionsE
                    filter i.question_1 == "Slower aggregation"
                    filter i.question_3 == "Yes"
                    return i"""
        q.custom_query(cls.database, query, "test_file", "tests\\test_json_data")

    @classmethod
    def tearDownClass(cls):
        client = ArangoClient()
        sys_db = client.db("_system", username=USERNAME, password=PASSWORD)
        sys_db.delete_database("testDB")

        files = os.listdir("../tests/test_json_data")
        for file in files:
            os.remove("../tests/test_json_data/" + file)

        files = os.listdir("test_vis_data")
        for file in files:
            os.remove("../tests/test_vis_data/" + file)

        os.remove("../tests/nx.html")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def test_graphviz_graph(self):
        v.graphviz_graph("test_file", input_dir="../tests/test_json_data", output_dir="test_vis_data")
        path = pl.Path("./test_vis_data/test_file.pdf")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

    def test_networkx_pyvis_graph(self):
        v.networkx_pyvis_graph("test_file", input_dir="../tests/test_json_data", output_dir="test_vis_data")
        path = pl.Path("../nx.html")
        self.assertEqual((str(path), path.is_file()), (str(path), True))


if __name__ == '__main__':
    unittest.main()
