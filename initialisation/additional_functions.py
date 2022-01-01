import json
import pandas as pd
import os.path
import re
import openpyxl


def open_excel_file(path, sheet):
    """ This method allows to open an Excel file and retrieve data from chosen sheet.

    :param path: (str) path of the file to open
    :param sheet: (str) name of the sheet to open
    :return: (DataFrame) data from chosen sheet
    """
    file = pd.ExcelFile(path)
    sheet = file.parse(sheet)
    return sheet


def check_for_greek(name):
    """This method checks if given amyloid name contains Greek letters and if yes, replaces them with name of the
    letter in Latin script.

    :param name: (str) name of the amyloid to check
    :return: (str)
    """
    if "\u03b1" in name or "\u0391" in name:
        return name.replace("\u03b1", "alpha").replace("\u0391", "alpha")
    elif "\u03b2" in name or "\u0392" in name:
        return name.replace("\u03b2", "beta").replace("\u0392", "beta")
    elif "\u03b3" in name or "\u0393" in name:
        return name.replace("\u03b3", "gamma").replace("\u0393", "gamma")
    elif "\u03b4" in name or "\u0394" in name:
        return name.replace("\u03b4", "delta").replace("\u0394", "delta")
    elif "\u03b5" in name or "\u0395" in name:
        return name.replace("\u03b5", "epsilon").replace("\u0395", "epsilon")
    elif "\u03b6" in name or "\u0396" in name:
        return name.replace("\u03b6", "zeta").replace("\u0396", "zeta")
    elif "\u03b7" in name or "\u0397" in name:
        return name.replace("\u03b7", "eta").replace("\u0397", "eta")
    elif "\u03b8" in name or "\u0398" in name:
        return name.replace("\u03b8", "theta").replace("\u0398", "theta")
    elif "\u03b9" in name or "\u0399" in name:
        return name.replace("\u03b9", "iota").replace("\u0399", "iota")
    elif "\u03ba" in name or "\u039a" in name:
        return name.replace("\u03ba", "kappa").replace("\u039a", "kappa")
    elif "\u03bb" in name or "\u039b" in name:
        return name.replace("\u03bb", "lambda").replace("\u039b", "lambda")
    elif "\u03bc" in name or "\u039c" in name:
        return name.replace("\u03bc", "mu").replace("\u039c", "mu")
    elif "\u03bd" in name or "\u039d" in name:
        return name.replace("\u03bd", "nu").replace("\u039d", "nu")
    elif "\u03be" in name or "\u039e" in name:
        return name.replace("\u03be", "xi").replace("\u039e", "xi")
    elif "\u03bf" in name or "\u039f" in name:
        return name.replace("\u03bf", "omicron").replace("\u039f", "omicron")
    elif "\u03c0" in name or "\u03a0" in name:
        return name.replace("\u03c0", "pi").replace("\u03a0", "pi")
    elif "\u03c1" in name or "\u03a1" in name:
        return name.replace("\u03c1", "rho").replace("\u03a1", "rho")
    elif "\u03c2" in name or "\u03a3" in name or "\u03c3":
        return name.replace("\u03c2", "sigma").replace("\u03a3", "sigma").replace("u03c3", "sigma")
    elif "\u03c4" in name or "\u03a4" in name:
        return name.replace("\u03c4", "tau").replace("\u03a4", "tau")
    elif "\u03c5" in name or "\u03a5" in name:
        return name.replace("\u03c5", "upsilon").replace("\u03a5", "upsilon")
    elif "\u03c6" in name or "\u03a6" in name:
        return name.replace("\u03c6", "phi").replace("\u03a6", "phi")
    elif "\u03c7" in name or "\u03a7" in name:
        return name.replace("\u03c7", "chi").replace("\u03a7", "chi")
    elif "\u03c8" in name or "\u03a8" in name:
        return name.replace("\u03c8", "psi").replace("\u03a8", "psi")
    elif "\u03c9" in name or "\u03a9" in name:
        return name.replace("\u03c9", "omega").replace("\u03a9", "omega")
    else:
        return name


def create_json(path, collection):
    """

    :param path:
    :param collection:
    """
    with open(path, 'w') as outfile:
        json.dump(collection, outfile)


def join_json(path, collection):
    """

    :param path:
    :param collection:
    """
    if os.path.isfile(path):
        with open(path, "r") as file:
            data = json.load(file)

        for i in collection:
            data.append(i)

        with open(path, "w") as outfile:
            json.dump(data, outfile)

    else:
        with open(path, "w") as outfile:
            json.dump(collection, outfile)


def get_temp(temp):
    """

    :param temp:
    :return:
    """
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
