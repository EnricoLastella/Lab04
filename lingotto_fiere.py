import csv

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome

        self.espositori = []
        self.stand = []

    @property
    def nome(self):

        return self._nome

    @nome.setter
    def nome(self, nuovo_nome):

        if nuovo_nome != "":
            self._nome = nuovo_nome
        else:
            raise ValueError ("IL NOME NON PUO ESSERE VUOTO")



    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:
            with open(file_path, "r", encoding="utf-8") as file:

                reader = csv.reader(file, delimiter=",")

                for riga in reader:

                    codice = riga[0].strip()

                    if codice.startswith("ES"):
                        nome = riga[1].strip()
                        cognome = riga[2].strip()
                        nuovo_espositore = Espositore(codice, nome, cognome)
                        self.espositori.append(nuovo_espositore)

                    if codice.startswith("ST"):
                        superficie = float(riga[1].strip())
                        padiglione = int(riga[2].strip())
                        prezzo_base = float(riga[3].strip())

                        if len(riga) == 4:
                            nuovo_stand = Stand(codice, superficie, padiglione, prezzo_base)
                            self.stand.append(nuovo_stand)

                        if len(riga) == 5:

                            extra = riga[4].strip()

                            if extra.isdigit():
                                n_prese = int(extra)
                                nuovo_stand = StandPreseExtra(codice, superficie, padiglione, prezzo_base, n_prese)
                                self.stand.append(nuovo_stand)

                            else:
                                posizione = extra
                                nuovo_stand = StandPremium(codice, superficie, padiglione, prezzo_base, posizione)
                                self.stand.append(nuovo_stand)

        except FileNotFoundError:
            raise FileNotFoundError


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""

        stand = None
        for elemento in self.stand:
            if codice_stand == elemento.codice:
                stand = elemento
                break

        espositore = None

        for esp in self.espositori:
            if codice_espositore == esp.codice:
                espositore = esp
                break

        if stand is None:

            raise ValueError ("STAND NON TROVATO")

        if espositore is None:

            raise ValueError ("ESPOSITORE NON TROVATO")

        if stand.espositore is not None:
                raise ValueError ("STAND OCCUPATO")

        if espositore.stand is not None:
                raise ValueError ("ESPOSITORE GIA ASSOCIATO A UNO STAND")

        stand.espositore = espositore

        espositore.stand = stand


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for esp in self.espositori:
            if esp.stand is None:
                print(f"{esp.nome} {esp.cognome} NON ASSOCIATO A NESSUNO STAND")
            else:
                print(f"{esp.nome} {esp.cognome} ASSSOCIATO ALLO STAND {esp.stand.codice}")


    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(self.stand)

class Espositore:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.stand = None

    def __str__(self):

        return f"Codice: {self.codice} Nome: {self.nome} Cognome: {self.cognome}"

class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self.codice = codice
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo_base = prezzo_base
        self.espositore = None


    def __str__(self):

        return f"{self.codice}: Standard | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.CalcolaPrezzo():.2f}€ - {self._stato()}"

    def CalcolaPrezzo(self):
        return self.prezzo_base

    def _stato(self):
        if self.espositore is None:
            return "Disponibile"
        else:
            return "Non disponibile"

    def __lt__(self, other):
        return self.CalcolaPrezzo() < other.CalcolaPrezzo()


class StandPreseExtra(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, n_prese):
        super().__init__(codice, superficie, padiglione, prezzo_base)

        self.n_prese = n_prese

    def CalcolaPrezzo(self):

        return self.prezzo_base*(1+0.07*self.n_prese)

    def __str__(self):
        return (f"{self.codice}: Prese Extra | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.CalcolaPrezzo():.2f}€ - Prese aggiuntive: {self.n_prese} - {self._stato()}")


class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
        super().__init__(codice, superficie, padiglione, prezzo_base)

        self.posizione = posizione

    def CalcolaPrezzo(self):

        return self.prezzo_base*1.3

    def __str__(self):
        return (f"{self.codice}: Premium | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.CalcolaPrezzo():.2f}€ - Posizione: {self.posizione} - {self._stato()}")
