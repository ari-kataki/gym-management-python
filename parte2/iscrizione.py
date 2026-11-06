from parte1.corso import Corso
from parte1.iscritto import Iscritto

valoriStatoIscrizione = {0: "attiva", 1: "chiusa"}

class Iscrizione:

    def __init__(self, iscritto: Iscritto, corso: Corso, statoIniziale = None):
        self.__iscritto = iscritto      # OGGETTO_A
        self.__corso = corso            # OGGETTO_B

        if statoIniziale == None:
            # MODALITA' NUOVA ISCRIZIONE
            if corso.isDisponibile():
                self.__stato = valoriStatoIscrizione[0]   # stato = attiva
                self.__corso.aggiungiPartecipante()         # cambia stato del corso
                self.__iscritto.aggiungiCorso(self.__corso) # aggiunge alla lista iscritto
            else:
                print(f"Errore: il corso '{corso.nome}' non e' disponibile per l'iscrizione!")
                self.__stato = valoriStatoIscrizione[1]   # stato = chiusa
        else:
            # MODALITA' CARICAMENTO DA FILE
            self.__stato = statoIniziale

    @property
    def iscritto(self):
        return self.__iscritto

    @property
    def corso(self):
        return self.__corso

    @property
    def stato(self):
        return self.__stato

    def disdiciIscrizione(self):
        if self.__stato == valoriStatoIscrizione[0]:      # se attiva
            self.__corso.rimuoviPartecipante()            # ripristina stato corso
            self.__iscritto.rimuoviCorso(self.__corso)    # rimuove da lista iscritto
            self.__stato = valoriStatoIscrizione[1]       # chiude l'iscrizione
        else:
            print("Errore: questa iscrizione e' gia' chiusa!")

    def isAttiva(self):
        return self.__stato == valoriStatoIscrizione[0]

    def __str__(self):
        return (f"~~~~~~~~~~~~~~~~\n"
                f"OGGETTO ISCRIZIONE\n"
                f"Iscritto: {self.__iscritto.codice} - {self.__iscritto.nome} {self.__iscritto.cognome}\n"
                f"Corso: {self.__corso.codice} - {self.__corso.nome}\n"
                f"Stato: {self.__stato}\n"
                f"~~~~~~~~~~~~~~~~\n")

if __name__ == "__main__":
    iscritto = Iscritto("I001", "Mario", "Rossi", 30)
    corso = Corso("C001", "Yoga", "Sara Rossi", 5)

    print(f"Stato corso prima dell'iscrizione: {corso.stato}")
    iscrizione = Iscrizione(iscritto, corso)
    print(f"Partecipanti corso dopo l'iscrizione: {corso.partecipantiAttuali}")
    print(iscrizione)
    iscrizione.disdiciIscrizione()
    print(f"Partecipanti corso dopo la disdetta: {corso.partecipantiAttuali}")
    print(iscrizione)
