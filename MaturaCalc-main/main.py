# Path: MaturaCalc/main.py
# wages = [G1, G2, JP, JO_P, JO_R, M_P, M_R]

import sys
import csv
from data import read_csv_file, return_result
from formulas import calculate
import scraper

if __name__ == "__main__":
    # dane podane przez użytkownika
    university = "AGH"  # uczelnia; AGH - test
    field_of_study = "Ceramika"  # kierunek; Ceramika - test
    #subjects = -1  # przedmioty

    version = "polska_nowa_matura"
    G1 = -1
    G2 = -1
    JP = -1 # jezyk polski
    JO_P = -1  # jezyk obcy podstawowy
    JO_R = -1 # jezyk obcy rozszerzony
    M_P = -1 # matematyka podstawowa
    M_R = -1 # matematyka rozszerzona
    wages = [G1, G2, JP, JO_P, JO_R, M_P, M_R]
    final_result = -1  # obliczony wynik

    universities = {
        "AGH": scraper.get_AGH,
        "Politechnika Krakowska": scraper.get_PolitechnikaKrakowska,
        "Politechnika Warszawska": scraper.get_PolitechnikaWarszawska,
        "Politechnika Wroclawska": scraper.get_PolitechnikaWroclawska,
        "Politechnika Poznanska": scraper.get_PolitechnikaPoznanska,
        "Politechnika Lodzka": scraper.get_PolitechnikaLodzka,
        "Politechnika Slaska": scraper.get_PolitechnikaSlaska,
        "Politechnika Opolska": scraper.get_PolitechnikaOpolska,
        "Politechnika Gdanska": scraper.get_PolitechnikaGdanska,
        "Politechnika Bialostocka": scraper.get_PolitechnikaBialostocka,
        "Politechnika Lubelska": scraper.get_PolitechnikaLubelska,
        "Politechnika Koszalinska": scraper.get_PolitechnikaKoszalinska,
        "Politechnika Rzeszowska": scraper.get_PolitechnikaRzeszowska,
        "Politechnika Szczecinska": scraper.get_PolitechnikaSzczecinska,
        "Politechnika Bydgoska": scraper.get_PolitechnikaBydgoska,
        "Politechnika Czestochowska": scraper.get_PolitechnikaCzestochowska
    }

    # pierwszy wiersz to wiersz nagłówkowy
    results = read_csv_file("results.csv")

    # pobieranie G1, G2 i reszty wag
    subjects1, subjects2 = universities[university](field_of_study)

    # obliczanie wyniku
    final_result = calculate(university, field_of_study, results, subjects1, subjects2)

    return_result(str(final_result), "1000", university, field_of_study)

'''
    # wybór wariantu obliczeń wyników
    versions = {0: "polska_nowa", 1: "polska_stara", 2: "zagraniczna", 3: "IB"}
    version_num = 0
    version = versions[version_num]

    # wybór uczelni
    universities = {0: "AGH", 1: "PolitechnikaKrakowska", 2: "PolitechnikaWroclawska", 3: "PolitechnikaWarszawska",
                    4: "PolitechnikaLodzka", 5: "PolitechnikaSlaska", 6: "PolitechnikaGdanska",
                    7: "PolitechnikaPoznanska", 8: "PolitechnikaSzczecińska"}
    university_num = 0
    university = universities[university_num]

    # przeliczenie wyników zagranicznych
    if version == "zagraniczna":
        for i in range(1, len(results)):
            results[i][2] = str(int(results[i][2]) + 20)
'''
