from parte1.persona import Persona

limiteCorsiIscritti = 3

class Iscritto(Persona):

    def __init__(self, codice, nome, cognome, eta):
        super().__init__(codice, nome, cognome)     # nel JSON non c'e' il codice fiscale: uso il codice iscritto come cF
        self.__eta = eta
        self.__corsiIscritti = list()

    @property
    def codice(self):
        return self.cF

    @property
    def eta(self):
        return self.__eta

    @eta.setter
    def eta(self, nuovaEta):
        self.__eta = nuovaEta

    # ----------------------------------------------------------
    # PROPERTY SOLA LETTURA - LISTA_OGGETTI_COLLEGATI
    # Non ha setter perche' la lista si modifica solo tramite metodi.
    # ----------------------------------------------------------
    @property
    def corsiIscritti(self):
        return self.__corsiIscritti

    # ----------------------------------------------------------
    # METODO: aggiunge un oggetto alla lista con controllo limite
    # PATTERN if/else: se sotto il limite aggiunge, altrimenti stampa errore.
    # ----------------------------------------------------------
    def aggiungiCorso(self, corso):
        if len(self.__corsiIscritti) < limiteCorsiIscritti:
            self.__corsiIscritti.append(corso)    # aggiunge alla lista
        else:
            print(f"Errore: l'iscritto {self.codice} ha gia' raggiunto il limite di {limiteCorsiIscritti} corsi!")

    # ----------------------------------------------------------
    # METODO: rimuove un oggetto dalla lista con controllo esistenza
    # ----------------------------------------------------------
    def rimuoviCorso(self, corso):
        if corso in self.__corsiIscritti:
            self.__corsiIscritti.remove(corso)
        else:
            print("Errore: l'iscritto non risulta iscritto a questo corso!")

    def numeroCorsiIscritti(self):
        return len(self.__corsiIscritti)

    def __str__(self):
        return (f"****************\n"
                f"OGGETTO ISCRITTO\n"
                f"Codice: {self.codice}\n"
                f"Nome: {self.nome}\n"
                f"Cognome: {self.cognome}\n"
                f"Eta': {self.__eta}\n"
                f"Corsi iscritti: {self.numeroCorsiIscritti()}/{limiteCorsiIscritti}\n"
                f"****************\n")

if __name__ == "__main__":
    numeroIscritti = int(input("Inserisci il numero di oggetti Iscritto da creare: "))
    listaIscritti = list()

    for i in range(numeroIscritti):
        codice = input(f"Inserisci il CODICE dell'iscritto numero {i + 1}: ")
        nome = input(f"Inserisci il NOME dell'iscritto numero {i + 1}: ")
        cognome = input(f"Inserisci il COGNOME dell'iscritto numero {i + 1}: ")
        eta = input(f"Inserisci l'ETA' dell'iscritto numero {i + 1}: ")
        iscritto = Iscritto(codice, nome, cognome, eta)
        listaIscritti.append(iscritto)

    for iscritto in listaIscritti:
        print(iscritto)
