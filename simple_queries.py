import json


def check_questions_simple(database, q1, q2, q3, filename="result"):
    aql = database.aql

    cursor = database.aql.execute(
        'FOR int IN interactionsE FILTER int.question_1 == @q1 FILTER int.question_2 == @q2 FILTER int.question_3 == @q3 RETURN int ',
        bind_vars={'q1': q1, 'q2': q2, 'q3': q3}
    )

    # interactionsE

    inter = [doc for doc in cursor]

    # for x in inter:
    #     print(x)

    with open(f"./json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)


