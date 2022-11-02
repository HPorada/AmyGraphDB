from queries_functions import save_function as save
from config.definitions import ROOT_DIR


def nearest_connections_graph(db, filename="result", directory=None, nodeID=None):
    cursor = db.aql.execute(
        """
        for v, e, p in 1..1 any @nodeID graph "ExtendedV2"
            return p
        """,
        bind_vars={'nodeID': nodeID}
    )

    inter = [i for i in cursor]
    save.save_query_result(ROOT_DIR, directory, filename, inter)