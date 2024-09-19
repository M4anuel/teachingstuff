import random
class Schueler:
    def __init__(self, name: str, geschlecht: chr, ansprechperson: str, geschlecht_ansprechperson: chr):
        self.name = name
        self.geschlecht = geschlecht
        self.ansprechperson = ansprechperson
        self.geschlecht_ansprechperson = geschlecht_ansprechperson


schueler = []
schueler.append(Schueler("Tim", "m", "Nelly", "w"))
schueler.append(Schueler("Tom", "m", "Nelly", "w"))


for schuel in schueler:
    print(schuel.name)