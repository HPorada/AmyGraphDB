import os
import json


def save_query_result(root, directory, filename, inter):
    """This method saves results of executed queries in chosen directory.

    :param root: (str) Root directory to create and use absolute paths.
    :param directory: (str) Directory where file is to be saved.
    :param filename: (str) Name of the file that is to be saved.
    :param inter: (list) List of the query results.
    """
    if directory is not None:
        with open(os.path.join(root, directory, f"{filename}.json"), "w") as outfile:
            json.dump(inter, outfile)
    else:
        with open(os.path.join(root, f"queries_functions\\json_data\\{filename}.json"), "w") as outfile:
            json.dump(inter, outfile)
