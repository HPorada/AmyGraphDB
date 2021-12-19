import json


def filter_simple(database, q1, q2, q3, filename="result"):
    aql = database.aql

    cursor = database.aql.execute(
        """for item in sequences
            for v, e, p in 1..1 any item._id graph "Simple"
                filter e.question_1 == @q1
                filter e.question_2 == @q2
                filter e.question_3 == @q3
                return p""",
        bind_vars={'q1': q1, 'q2': q2, 'q3': q3}
    )

    # interactionsE

    inter = [doc for doc in cursor]

    for x in inter:
        print(x)

    # with open(f"./json_data/{filename}.json", "w") as outfile:
    #     json.dump(inter, outfile)


