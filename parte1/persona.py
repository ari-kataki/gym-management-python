class Persona:
    def __init__(self, cF, nome, cognome):
        self.__cF = cF
        self.__nome = nome
        self.__cognome = cognome

    @property
    def cF(self):
        return self.__cF

    @cF.setter
    def cF(self, nuovoCF):
        self.__cF = nuovoCF

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nuovoNome):
        self.__nome = nuovoNome

    @property
    def cognome(self):
        return self.__cognome

    @cognome.setter
    def cognome(self, nuovoCognome):
        self.__cognome = nuovoCognome

    def __str__(self):
        return (f"****************\n"
                f"OGGETTO PERSONA\n"
                f"Codice Fiscale: {self.__cF}\n"
                f"Nome: {self.__nome}\n"
                f"Cognome: {self.__cognome}\n"
                f"****************\n")

if __name__ == "__main__":
    numeroPersone = int(input("Inserisci il numero di oggetti Persona da creare: "))
    listaPersone = list()

    for i in range(numeroPersone):
        cF = input(f"Inserisci il CODICE FISCALE della persona numero {i + 1}: ")
        nome = input(f"Inserisci il NOME della persona numero {i + 1}: ")
        cognome = input(f"Inserisci il COGNOME della persona numero {i + 1}: ")
        persona = Persona(cF, nome, cognome)
        listaPersone.append(persona)

    for persona in listaPersone:
        print(persona)