from arango import ArangoClient

client = ArangoClient(hosts='http://localhost:8529')

sys_db = client.db('_system', username='root', password='Amyloids')

# Simple & Extended
db_Sep = client.db('AmyloidsSep', username='root', password='Amyloids')

# ExtendedE
db_Nov = client.db('AmyloidsNov', username='root', password='Amyloids')


# print(db.graph('ExtendedWithEdges'))
# graph = db.graph('ExtendedWithEdges')


def check_questions_simple(database, q1, q2, q3):
    aql = database.aql

    cursor = database.aql.execute(
        'FOR int IN interactions FILTER int.question_1 == @q1 FILTER int.question_2 == @q2 FILTER int.question_3 == @q3 RETURN int ',
        bind_vars={'q1': q1, 'q2': q2, 'q3': q3}
    )

    # interactionsE

    inter = [doc for doc in cursor]

    for x in inter:
        print(x)


def search_for_fragment(database, fragment):
    aql = database.aql

    cursor = database.aql.execute(
        'for i in sequences filter contains(i.sequence, @fragment) return i',
        bind_vars={'fragment': fragment}
    )

    # simpleView / sequencesE / extendedView

    inter = [doc for doc in cursor]

    for x in inter:
        print(x)


def search_for_key_word(database, key_word):
    aql = database.aql

    cursor = database.aql.execute(
        'for i in simpleView search phrase(i.general_remarks, @key, \'text_en\') return i',
        bind_vars={'key': key_word}
    )

    # extendedView

    inter = [doc for doc in cursor]

    for x in inter:
        print(x)


def search_for_all_connected(database, starting_amyloid):
    aql = database.aql

    cursor = database.aql.execute(
        'for v, p in 1..1 outbound @start amyseq return p',
        bind_vars={'start': starting_amyloid}
    )

    # amyseqE

    inter = [doc for doc in cursor]

    for x in inter:
        print(x)


def search_for_most_common(database, limit, type):  # type interactor lub interactee
    aql = database.aql

    cursor = database.aql.execute(
        "for int in intseqE filter int.type == @type collect sequence = int._from with count into total sort total desc limit @limit return{ \'sequence\': sequence, \'uses\': total}",
        bind_vars={'type': type, 'limit': limit}
    )

    inter = [doc for doc in cursor]

    for x in inter:
        print(x)


# check_questions_simple(db_Sep, "Faster aggregation", "Yes; implied by kinetics.", "No information")
# search_for_fragment(db_Sep, 'DAEFRHDSGY')
# search_for_key_word(db_Sep, 'pH')
# search_for_all_connected(db_Sep, 'amyloids/IAPP')
search_for_most_common(db_Sep, 10, 'interactor')