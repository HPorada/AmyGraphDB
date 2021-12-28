import json
import pandas as pd
import os.path
import re
import openpyxl


def open_questionnaire(path):
    file = pd.ExcelFile(path)
    sheet = file.parse("Form Responses 1")
    return sheet


def open_experiments(path):
    file = pd.ExcelFile(path)
    sheet_amyloids = file.parse("Lifestyle")
    sheet_interactions = file.parse("ATR_FTIR")
    return sheet_amyloids, sheet_interactions


def check_for_greek(name):
    if "\u03b1" in name:
        return name.replace("\u03b1", "alpha")
    elif "\u03b2" in name:
        return name.replace("\u03b2", "beta")
    elif "\u03b3" in name:
        return name.replace("\u03b3", "gamma")
    elif "\u03b4" in name:
        return name.replace("\u03b4", "delta")
    elif "\u03ba" in name:
        return name.replace("\u03ba", "kappa")
    else:
        return name


def create_json(path, dictionary):
    with open(path, 'w') as outfile:
        json.dump(dictionary, outfile)


def join_json(path, dictionary):
    if os.path.isfile(path):
        with open(path, "r") as file:
            data = json.load(file)

        for i in dictionary:
            data.append(i)

        with open(path, "w") as outfile:
            json.dump(data, outfile)

    else:
        with open(path, "w") as outfile:
            json.dump(dictionary, outfile)


def get_temp(temp):
    temps = re.findall(r"\d*\.\d+|\d+", temp)

    results = []

    for t in temps:
        if float(t) <= 10:
            results.append("psychrophilic")
        elif 10 < float(t) <= 45:
            results.append("mesophilic")
        elif 46 < float(t) <= 75:
            results.append("thermophilic")
        elif float(t) > 75:
            results.append("hyperthermophilic")
        else:
            results.append("error")

    return results


def get_ph(pH):
    phs = re.findall(r"\d+\.\d+", pH)

    results = []

    for p in phs:
        if float(p) < 5:
            results.append("acidophilic")
        elif 5 <= float(p) <= 9:
            results.append("neutrophilic")
        elif float(p) > 9:
            results.append("alkaliphilic")
        else:
            results.append("error")

    return results
