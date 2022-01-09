import os
import json


def save_query_result(root, directory, filename, inter):
    if directory is not None:
        with open(os.path.join(root, directory, f"{filename}.json"), "w") as outfile:
            json.dump(inter, outfile)
    else:
        with open(os.path.join(root, f"queries_functions\\json_data\\{filename}.json"), "w") as outfile:
            json.dump(inter, outfile)
