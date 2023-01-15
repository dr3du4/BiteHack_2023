# Path: MaturoCalc/formulas.py


def calculate(university, field_of_study, results1, results2, subjects):
    var = -1

    # AGH
    if university == "AGH":
        G1 = 0
        G2 = 0
        M = 0

        if field_of_study not in ["Ceramika", "Informatyka Społeczna", "Socjologia", "Kulturoznawstwo"]:
            print(results1)
            for result in results1:
                print(subjects[2])
                if result[0] in subjects:
                    if result[2] * 3 > G1:
                        G1 = result[2] * 3
                    elif result[2] > G2:
                        G2 = result[2]

                    if result[0] == "Matematyka" and result[1] == "Podstawowy":
                        M = result[2]

            return (G1 * 3 + G2 + M) * 2
        else:
            for result in results1:
                if result[0] in subjects:
                    if result[0] == "Matematyka" and result[1] == "Podstawowy":
                        M = int(result[2])
                    elif int(result[2]) > G1:
                        G1 = int(result[2])
                    elif int(result[2]) > G2:
                        G2 = int(result[2])

            return (G1 * 3 + G2 + M) * 2




    elif university == "PolitechnikaLodzka":
        results = args[0] + args[1]
        return results
'''
    # Politechnika Wroclawska
    elif university == "PolitechnikaWroclawska":
        results = args[0] + args[1]
        return results

    # Politechnika Warszawska
    elif university == "PolitechnikaWarszawska":
        results = args[0] + args[1]
        return results

    # Politechnika Lodzka
    elif university == "PolitechnikaLodzka":
        results = args[0] + args[1]
        return results

    # Politechnika Slaska
    elif university == "PolitechnikaSlaska":
        results = args[0] + args[1]
        return results

    # Politechnika Gdanska
    elif university == "PolitechnikaGdanska":
        results = args[0] + args[1]
        return results

    # Politechnika Poznanska
    elif university == "PolitechnikaPoznanska":
        results = args[0] + args[1]
        return results

    # Politechnika Szczecińska
    elif university == "PolitechnikaSzczecińska":
        results = args[0] + args[1]
        return results

    else:
        print("Nie ma takiej uczelni")
        '''
