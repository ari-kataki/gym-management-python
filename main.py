import json

from parte1.iscritto import Iscritto
from parte1.corso import Corso
from parte2.iscrizione import Iscrizione, valoriStatoIscrizione

fileJSON = "datiPalestra.json"

dataBase = {
    "iscritti": [],
    "corsi": [],
    "iscrizioni": []
}

def trovaIscritto(codice):
    oggettoIscritto = None
    for iscritto in dataBase["iscritti"]:
        if iscritto.codice == codice:
            oggettoIscritto = iscritto
    return oggettoIscritto

def trovaCorso(codice):
    oggettoCorso = None
    for corso in dataBase["corsi"]:
        if corso.codice == codice:
            oggettoCorso = corso
    return oggettoCorso

def caricaDati():
    try:
        with open(fileJSON, "r") as file:
            data = json.load(file)

        for i in data["iscritti"]:
            dataBase["iscritti"].append(Iscritto(i["codice"], i["nome"], i["cognome"], i["eta"]))

        for c in data["corsi"]:
            dataBase["corsi"].append(Corso(c["codice"], c["nome"], c["istruttore"], c["max_partecipanti"]))

        # le iscrizioni attive riempiono i corsi e le liste degli iscritti
        for s in data["iscrizioni"]:
            oggettoIscritto = trovaIscritto(s["codice_iscritto"])
            oggettoCorso = trovaCorso(s["codice_corso"])

            if oggettoIscritto != None and oggettoCorso != None:
                iscrizione = Iscrizione(oggettoIscritto, oggettoCorso, s["stato"])    # modalita' caricamento
                if s["stato"] == valoriStatoIscrizione[0]:
                    oggettoCorso.aggiungiPartecipante()
                    oggettoIscritto.aggiungiCorso(oggettoCorso)
                dataBase["iscrizioni"].append(iscrizione)

        print("Dati caricati con successo!")
    except:
        print("Errore nel caricamento del file!")

# Main minimale: carica il JSON, stampa tutto e prova una iscrizione.
# Il menu completo non e' stato scritto.
def main():
    caricaDati()

    for iscritto in dataBase["iscritti"]:
        print(iscritto)
    for corso in dataBase["corsi"]:
        print(corso)

    iscritto = trovaIscritto("I002")
    corso = trovaCorso("C002")
    if iscritto != None and corso != None:
        iscrizione = Iscrizione(iscritto, corso)
        dataBase["iscrizioni"].append(iscrizione)
        print(iscrizione)

if __name__ == "__main__":
    main()
