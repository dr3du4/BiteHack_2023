# Path: MaturaCalc/data.py

simplyString="sadasdasd"


# wczytywanie danych z pliku
def read_csv_file(filename):
    data = []

    with open(filename, "r") as file:
        for row in file:
            data.append(row.strip().split(";"))

    return data


# zwracanie wyniku (string)
def return_result(points_get, points_max, university, field_of_study):
    # PRINT W CELACH TESTOWYCH
    print("Zdobyto: " + points_get + "/" + points_max + " pkt na uczelni: " + university + ", na kierunku: " + field_of_study)
    return "Zdobyto: " + points_get + "/" + points_max + " pkt na uczelni: " + university + ", na kierunku: " + field_of_study


