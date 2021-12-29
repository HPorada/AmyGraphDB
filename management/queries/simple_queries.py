import json


def custom_query(database, query, filename="result"):
    cursor = database.aql.execute(query)

    inter = [doc for doc in cursor]

    with open(f"./management/json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)


def filter_questions_simple(database, q1, q2, q3, filename="result"):
    cursor = database.aql.execute(
        """for item in sequences
            for v, e, p in 1..1 any item._id graph "Simple"
                filter e.question_1 == @q1
                filter e.question_2 == @q2
                filter e.question_3 == @q3
                return p""",
        bind_vars={'q1': q1, 'q2': q2, 'q3': q3}
    )

    inter = [doc for doc in cursor]

    with open(f"./management/json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)


def contains_fragment_simple(database, fragment, filename="result"):
    cursor = database.aql.execute(
        """for item in sequences
            for v, e, p in 1..1 any item._id graph "Simple"
                filter contains(item.sequence, @fragment)
                return p""",
        bind_vars={'fragment': fragment}
    )

    inter = [doc for doc in cursor]

    with open(f"./management/json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)


def search_phrase_simple(database, key, filename="result"):
    cursor = database.aql.execute(
        """
        let items = (
            for i in simpleView
                search phrase(i.general_remarks, @key, 'text_en')
                return i
        )
        
        for i in sequences
            for v, e, p in 1..1 any i._id graph "Simple"
                for item in items
                    filter i._id == item._from or i._id == item._to
                    return p""",
        bind_vars={'key': key}
    )

    inter = [doc for doc in cursor]

    with open(f"./management/json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)

# def search_connected_simple(database, collection, start, filename="result"):
#     ()
