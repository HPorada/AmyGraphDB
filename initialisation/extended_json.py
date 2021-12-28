import json
import os.path

import initialisation.additional_functions as add


def questionnaire_extended():
    files = os.listdir('./initialisation/extended')

    for file in files:
        os.remove('./initialisation/extended/' + file)

    sheet = add.open_questionnaire("./initialisation/data/questionnaire.xlsx")

    # Dictionaries in lists
    seq_list = []
    sequences = []
    # _key, _id, sequence
    interactions = []
    # _key, _id, q1, q2, q3, general remarks, DOI
    amy_list = []
    amyloids = []
    # _key, _id, name
    amyseq = []
    # _from, _to
    seqint = []
    # _from, _to, type

    seq_num = 1
    int_num = 1

    for row in sheet.itertuples():
        # Answer to the first question: Is the interactor affecting interactee’s aggregating speed?
        q1 = str(row[3])

        # Answer to the second question: If interactee is still forming fibrils after the interaction, do fibrils of
        # interactee elongates by attaching to monomers/oligomers/fibrils of interactor?
        q2 = str(row[6])

        # Answer to the third question: Is interaction resulting in heterogeneous fibrils consisting of interactor and
        # interactee molecules?
        q3 = str(row[9])

        # Amyloid which is affecting the interactee
        interactor = str(row[12])

        # Sequence of the interactor
        seq1 = str(row[13])

        # Amyloid affected by the interactor
        interactee = str(row[14])

        # Sequence of the interactee
        seq2 = str(row[15])

        # Digital Object Identifier of the publication
        doi = str(row[16])

        # Other important remarks about the interaction
        general = str(row[17])

        if interactor not in amy_list:
            amy_list.append(interactor)
            amyloids.append(
                {
                    "_key": add.check_for_greek(interactor).replace(" ", "_"),
                    "_id": "amyloidsE/" + add.check_for_greek(interactor).replace(" ", "_"),
                    "name": interactor,
                }
            )

        if interactee not in amy_list:
            amy_list.append(interactee)
            amyloids.append(
                {
                    "_key": add.check_for_greek(interactee).replace(" ", "_"),
                    "_id": "amyloidsE/" + add.check_for_greek(interactee).replace(" ", "_"),
                    "name": interactee,
                }
            )

        if seq1 not in seq_list:
            seq_list.append(seq1)
            sequences.append(
                {
                    "_key": str(seq_num),
                    "_id": "sequencesE/" + str(seq_num),
                    "sequence": seq1
                }
            )

            amyseq.append(
                {
                    "_from": "amyloidsE/" + add.check_for_greek(interactor).replace(" ", "_"),
                    "_to": "sequencesE/" + str(seq_num)
                }
            )
            seq_num += 1

        if seq2 not in seq_list:
            seq_list.append(seq2)
            sequences.append(
                {
                    "_key": str(seq_num),
                    "_id": "sequencesE/" + str(seq_num),
                    "sequence": seq2
                }
            )

            amyseq.append(
                {
                    "_from": "amyloidsE/" + add.check_for_greek(interactee).replace(" ", "_"),
                    "_to": "sequencesE/" + str(seq_num)
                }
            )
            seq_num += 1

        sequence1 = seq_list.index(seq1)
        seq1_id = sequences[sequence1]["_id"]

        sequence2 = seq_list.index(seq2)
        seq2_id = sequences[sequence2]["_id"]

        interactions.append(
            {
                "_key": str(int_num),
                "_id": "interactionsE/" + str(int_num),
                "question_1": q1,
                "question_2": q2,
                "question_3": q3,
                "general_remarks": general,
                "DOI": doi
            }
        )

        seqint.append(
            {
                "_from": seq1_id,
                "_to": "interactionsE/" + str(int_num),
                "type": "interactor"
            }
        )

        seqint.append(
            {
                "_from": seq2_id,
                "_to": "interactionsE/" + str(int_num),
                "type": "interactee"
            }
        )

        int_num += 1

    add.create_json("./initialisation/extended/amyloidsE.json", amyloids)
    add.create_json("./initialisation/extended/sequencesE.json", sequences)
    add.create_json("./initialisation/extended/interactionsE.json", interactions)
    add.create_json("./initialisation/extended/amyseqE.json", amyseq)
    add.create_json("./initialisation/extended/seqintE.json", seqint)


def experiments_extended():
    sheet_amyloids, sheet_interactions = add.open_experiments("./initialisation/data/experiments.xlsx")

    # Dictionaries in lists
    seq_list = []
    sequences = []
    # _key, _id, sequence
    interactions = []
    # _key, _id, q1, q2, q3, general remarks, DOI
    amy_list = []
    amyloids = []
    # _key, _id, name
    amyseq = []
    # _from, _to
    seqint = []
    # _from, _to, type

    org_list = []
    organisms = []
    # _key, _id, name, lifestyle, temperature, pH
    orgamy = []
    # _from, _to

    int_num = 1

    # If file with interactions from questionnaire already exists: get the number of records there
    if os.path.isfile("./initialisation/extended/interactionsE.json"):
        with open("./initialisation/extended/interactionsE.json") as file:
            data = json.load(file)
            int_num = len(data)
            int_num += 1

    for row in sheet_amyloids.itertuples():

        id = str(row[2])

        sequence_name = str(row[3])

        sequence = str(row[4])

        formula = str(row[5])

        mass = str(row[6])

        amyloid_name = str(row[7])

        organism = str(row[9]).replace(" / ", "/")

        lifestyle = str(row[10])

        temperature = str(row[11])

        pH = str(row[12])

        if amyloid_name not in amy_list:
            amy_list.append(amyloid_name)
            amyloids.append(
                {
                    "_key": amyloid_name,
                    "_id": "amyloidsE/" + amyloid_name,
                    "name": amyloid_name,
                }
            )

        if sequence not in seq_list:
            seq_list.append(sequence)
            sequences.append(
                {
                    "_key": id,
                    "_id": "sequencesE/" + id,
                    "sequence": sequence,
                    "name": sequence_name,
                    "formula": formula,
                    "mass_M": mass,
                    "organism": organism,
                }
            )

            amyseq.append(
                {
                    "_from": "amyloidsE/" + amyloid_name,
                    "_to": "sequencesE/" + id,
                }
            )

        if organism not in org_list:
            org_list.append(organism)
            organisms.append(
                {
                    "_key": organism.replace(" ", "_").replace(".", "").replace("-", "_").replace("(", "").replace(")", "").replace("/", "_"),
                    "_id": "organismsE/" + organism.replace(" ", "_").replace(".", "").replace("-", "_").replace("(", "").replace(")", "").replace("/", "_"),
                    "lifestyle": lifestyle,
                    "temperature": temperature,
                    "pH": pH,
                }
            )

            orgamy.append(
                {
                    "_from": "organismsE/" + organism.replace(" ", "_").replace(".", "").replace("-", "_").replace("(", "").replace(")", "").replace("/", "_"),
                    "_to": "amyloidsE/" + amyloid_name,
                }
            )

    for row in sheet_interactions.itertuples():

        id = str(row[2])

        medium = str(row[4])

        concentration = str(row[5])

        age = str(row[6])

        temperature = str(row[7])

        parameters = str(row[8])

        amide = str(row[9])

        structure = str(row[10])

        comments = str(row[11])

        if "+" in id:
            new_str = ''.join((ch if ch in '0123456789' else ' ') for ch in id)
            num_list = [int(i) for i in new_str.split()]

            interactions.append(
                {
                    "_key": str(int_num),
                    "_id": "interactionsE/" + str(int_num),
                    "medium": medium,
                    "concentration": concentration,
                    "age": age,
                    "temperature": temperature,
                    "parameters": parameters,
                    "amide": amide,
                    "structure": structure,
                    "comments": comments,
                }
            )

            seqint.append(
                {
                    "_from": "sequencesE/PPT_" + str(num_list[0]),
                    "_to": "interactionsE/" + str(int_num),
                    "type": "interactor",
                }
            )

            seqint.append(
                {
                    "_from": "sequencesE/PPT_" + str(num_list[1]),
                    "_to": "interactionsE/" + str(int_num),
                    "type": "interactee",
                }
            )

            int_num += 1

        else:
            interactions.append(
                {
                    "_key": str(int_num),
                    "_id": "interactionsE/" + str(int_num),
                    "medium": medium,
                    "concentration": concentration,
                    "age": age,
                    "temperature": temperature,
                    "parameters": parameters,
                    "amide": amide,
                    "structure": structure,
                    "comments": comments,
                }
            )

            seqint.append(
                {
                    "_from": "sequencesE/" + str(id),
                    "_to": "interactionsE/" + str(int_num),
                    "type": "interactor",
                }
            )

            seqint.append(
                {
                    "_from": "sequencesE/" + str(id),
                    "_to": "interactionsE/" + str(int_num),
                    "type": "interactee",
                }
            )

            int_num += 1

    add.join_json("./initialisation/extended/amyloidsE.json", amyloids)
    add.join_json("./initialisation/extended/sequencesE.json", sequences)
    add.join_json("./initialisation/extended/interactionsE.json", interactions)
    add.join_json("./initialisation/extended/amyseqE.json", amyseq)
    add.join_json("./initialisation/extended/seqintE.json", seqint)
    add.join_json("./initialisation/extended/organismsE.json", organisms)
    add.join_json("./initialisation/extended/orgamyE.json", orgamy)
