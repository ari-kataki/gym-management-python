# DIZIONARIO DI MODULO - valori possibili dello stato del corso
valoriStatoCorso = {0: "disponibile", 1: "completo"}

class Corso:

    def __init__(self, codice, nome, istruttore, maxPartecipanti):
        self.__codice = codice
        self.__nome = nome
        self.__istruttore = istruttore
        self.__maxPartecipanti = maxPartecipanti
        self.__partecipantiAttuali = 0
        self.__stato = valoriStatoCorso[0]      # stato iniziale sempre = default

    @property
    def codice(self):
        return self.__codice

    @codice.setter
    def codice(self, nuovoCodice):
        self.__codice = nuovoCodice

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nuovoNome):
        self.__nome = nuovoNome

    @property
    def istruttore(self):
        return self.__istruttore

    @istruttore.setter
    def istruttore(self, nuovoIstruttore):
        self.__istruttore = nuovoIstruttore

    @property
    def maxPartecipanti(self):
        return self.__maxPartecipanti

    @property
    def partecipantiAttuali(self):
        return self.__partecipantiAttuali

    # Lo stato NON ha setter: cambia solo tramite aggiungiPartecipante() e rimuoviPartecipante()
    @property
    def stato(self):
        return self.__stato

    def aggiungiPartecipante(self):
        if self.__partecipantiAttuali < self.__maxPartecipanti:
            self.__partecipantiAttuali += 1
            if self.__partecipantiAttuali == self.__maxPartecipanti:
                self.__stato = valoriStatoCorso[1]
        else:
            print(f"Errore: il corso '{self.__nome}' e' gia' completo!")

    def rimuoviPartecipante(self):
        if self.__partecipantiAttuali > 0:
            self.__partecipantiAttuali -= 1
            self.__stato = valoriStatoCorso[0]
        else:
            print(f"Errore: il corso '{self.__nome}' non ha partecipanti!")

    def isDisponibile(self):
        return self.__stato == valoriStatoCorso[0]

    def __str__(self):
        return (f"----------------\n"
                f"OGGETTO CORSO\n"
                f"Codice: {self.__codice}\n"
                f"Nome: {self.__nome}\n"
                f"Istruttore: {self.__istruttore}\n"
                f"Partecipanti: {self.__partecipantiAttuali}/{self.__maxPartecipanti}\n"
                f"Stato: {self.__stato}\n"
                f"----------------\n")

if __name__ == "__main__":
    corso1 = Corso("C001", "Yoga", "Sara Rossi", 2)
    print(corso1)
    corso1.aggiungiPartecipante()
    corso1.aggiungiPartecipante()
    corso1.aggiungiPartecipante()
    print(f"Stato corso1 dopo le iscrizioni: {corso1.stato}")
