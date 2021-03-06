import os
import sys

sys.path.append("../")
sys.path.append("../initialisation_functions")

from initialisation_functions import additional_functions as add


def questionnaire_simple(input_file, output_dir="../initialisation_functions/simple/", join=False):
    """This method generates JSON files from Excel files with questionnaire data for SIMPLE database structure.

    :param input_file: (str) Path to the Excel file with questionnaire data.
    :param output_dir: (str) Path to the directory where JSON files are to be saved.
    :param join: (boolean) Default: False - files existing in the directory before method's executions are deleted.
    """
    files = os.listdir(output_dir)

    if not join:
        for file in files:
            os.remove(output_dir + "/" + file)

    sheet = add.open_excel_file(input_file, "Form Responses 1")

    # Dictionaries in lists
    seq_list = []
    sequences = []
    # _key, _id, sequence
    interactions = []
    # _from, _to, q1, q2, q3, general remarks, DOI
    amy_list = []
    amyloids = []
    # _key, _id, name
    amyseq = []
    # _from, _to

    seq_num = 1

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
                    "_id": "amyloids/" + add.check_for_greek(interactor).replace(" ", "_"),
                    "name": interactor,
                }
            )

        if interactee not in amy_list:
            amy_list.append(interactee)
            amyloids.append(
                {
                    "_key": add.check_for_greek(interactee).replace(" ", "_"),
                    "_id": "amyloids/" + add.check_for_greek(interactee).replace(" ", "_"),
                    "name": interactee,
                }
            )

        if seq1 not in seq_list:
            seq_list.append(seq1)
            sequences.append(
                {
                    "_key": str(seq_num),
                    "_id": "sequences/" + str(seq_num),
                    "sequence": seq1
                }
            )

            amyseq.append(
                {
                    "_from": "amyloids/" + add.check_for_greek(interactor).replace(" ", "_"),
                    "_to": "sequences/" + str(seq_num)
                }
            )
            seq_num += 1

        if seq2 not in seq_list:
            seq_list.append(seq2)
            sequences.append(
                {
                    "_key": str(seq_num),
                    "_id": "sequences/" + str(seq_num),
                    "sequence": seq2
                }
            )

            amyseq.append(
                {
                    "_from": "amyloids/" + add.check_for_greek(interactee).replace(" ", "_"),
                    "_to": "sequences/" + str(seq_num)
                }
            )
            seq_num += 1

        sequence1 = seq_list.index(seq1)
        seq1_id = sequences[sequence1]["_id"]

        sequence2 = seq_list.index(seq2)
        seq2_id = sequences[sequence2]["_id"]

        interactions.append(
            {
                "_from": seq1_id,
                "_to": seq2_id,
                "question_1": q1,
                "question_2": q2,
                "question_3": q3,
                "general_remarks": general,
                "DOI": doi
            }
        )

    if not join:
        add.create_json(f"{output_dir}/amyloids.json", amyloids)
        add.create_json(f"{output_dir}/sequences.json", sequences)
        add.create_json(f"{output_dir}/interactions.json", interactions)
        add.create_json(f"{output_dir}/amyseq.json", amyseq)
    else:
        add.join_json(f"{output_dir}/amyloids.json", amyloids)
        add.join_json(f"{output_dir}/sequences.json", sequences)
        add.join_json(f"{output_dir}/interactions.json", interactions)
        add.join_json(f"{output_dir}/amyseq.json", amyseq)


def experiments_simple(input_file, output_dir="../initialisation_functions/simple", join=True):
    """This method generates JSON files from Excel files with data from electronic laboratory log for SIMPLE database structure.

    :param input_file: (str) Path to the Excel file with data from electronic laboratory log.
    :param output_dir: (str) Path to the directory where JSON files are to be saved.
    :param join: (boolean) Default: True - new data is joined with files existing in the directory before method's execution.
    """
    # sheet_amyloids, sheet_interactions = add.open_experiments("../initialisation_functions/data/experiments.xlsx")

    files = os.listdir(output_dir)

    if not join:
        for file in files:
            os.remove(output_dir + "/" + file)

    sheet_amyloids = add.open_excel_file(input_file, "Lifestyle")
    sheet_interactions = add.open_excel_file(input_file, "ATR_FTIR")

    # Dictionaries in lists
    seq_list = []
    sequences = []
    # _key, _id, sequence
    interactions = []
    # _from, _to, q1, q2, q3, general remarks, DOI

    amy_list = []
    amyloids = []
    # _key, _id, name
    amyseq = []
    # _from, _to

    org_list = []
    organisms = []
    # _key, _id, name, lifestyle, temperature, pH
    orgamy = []
    # _from, _to

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
                    "_id": "amyloids/" + amyloid_name,
                    "name": amyloid_name,
                }
            )

        if id not in seq_list:
            seq_list.append(id)
            sequences.append(
                {
                    "_key": id,
                    "_id": "sequences/" + id,
                    "sequence": sequence,
                    "name": sequence_name,
                    "formula": formula,
                    "mass_M": mass,
                    "organism": organism,
                }
            )

            amyseq.append(
                {
                    "_from": "amyloids/" + amyloid_name,
                    "_to": "sequences/" + id,
                }
            )

        if organism not in org_list:
            org_list.append(organism)
            organisms.append(
                {
                    "_key": organism.replace(" ", "_").replace(".", "").replace("-", "_").replace("(", "").replace(")",
                                                                                                                   "").replace(
                        "/", "_"),
                    "_id": "organisms/" + organism.replace(" ", "_").replace(".", "").replace("-", "_").replace("(",
                                                                                                                "").replace(
                        ")", "").replace("/", "_"),
                    "lifestyle": lifestyle,
                    "temperature": temperature,
                    "pH": pH,
                }
            )

            orgamy.append(
                {
                    "_from": "organisms/" + organism.replace(" ", "_").replace(".", "").replace("-", "_").replace("(",
                                                                                                                  "").replace(
                        ")", "").replace("/", "_"),
                    "_to": "amyloids/" + amyloid_name,
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
                    "_from": "sequences/PPT_" + str(num_list[0]),
                    "_to": "sequences/PPT_" + str(num_list[1]),
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
        else:
            interactions.append(
                {
                    "_from": "sequences/" + id,
                    "_to": "sequences/" + id,
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

    if not join:
        add.create_json(f"{output_dir}/amyloids.json", amyloids)
        add.create_json(f"{output_dir}/sequences.json", sequences)
        add.create_json(f"{output_dir}/interactions.json", interactions)
        add.create_json(f"{output_dir}/amyseq.json", amyseq)
        add.create_json(f"{output_dir}/organisms.json", organisms)
        add.create_json(f"{output_dir}/orgamy.json", orgamy)
    else:
        add.join_json(f"{output_dir}/amyloids.json", amyloids)
        add.join_json(f"{output_dir}/sequences.json", sequences)
        add.join_json(f"{output_dir}/interactions.json", interactions)
        add.join_json(f"{output_dir}/amyseq.json", amyseq)
        add.join_json(f"{output_dir}/organisms.json", organisms)
        add.join_json(f"{output_dir}/orgamy.json", orgamy)
