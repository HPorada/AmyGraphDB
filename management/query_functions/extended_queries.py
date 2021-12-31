import json


def filter_questions_extended(database, q1, q2, q3, filename="result", directory=None):
    cursor = database.aql.execute(
        """for item in interactionsE
            for v, e, p in 1..1 any item._id graph "Extended"
                filter item.question_1 == @q1
                filter item.question_2 == @q2
                filter item.question_3 == @q3
                return p""",
        bind_vars={'q1': q1, 'q2': q2, 'q3': q3}
    )

    inter = [doc for doc in cursor]

    if directory is not None:
        with open(f"{directory}/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)
    else:
        with open(f"./management/json_data/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)


def contains_fragment_extended(database, fragment, filename="result", directory=None):
    cursor = database.aql.execute(
        """for item in sequencesE
            for v, e, p in 1..1 any item._id graph "Extended"
                filter contains(item.sequence, @fragment)
                return p""",
        bind_vars={'fragment': fragment}
    )

    inter = [doc for doc in cursor]

    if directory is not None:
        with open(f"{directory}/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)
    else:
        with open(f"./management/json_data/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)


def search_phrase_extended(database, keyword, filename="result", directory=None):
    cursor = database.aql.execute(
        """
        let items = (
            for i in extendedView 
                search phrase(i.general_remarks, @keyword, 'text_en') 
                return i
        )

        for item in items
            for v, e, p in 1..1 any item._id graph "Extended"
                return p""",
        bind_vars={'keyword': keyword}
    )

    inter = [doc for doc in cursor]

    if directory is not None:
        with open(f"{directory}/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)
    else:
        with open(f"./management/json_data/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)

# def search_connected_extended(database, collection, start, filename="result"):
#     ()
#