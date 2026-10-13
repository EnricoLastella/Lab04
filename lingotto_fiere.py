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
            raise TypeError



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

                    if codice.startswith("ST"):
                        superficie = float((riga[1].strip))
                        padiglione = int((riga[2].strip))
                        prezzo_base = float(riga[3].strip())

                    if len(riga) == 4:
                        nuovo_stand = Stand(codice, superficie, padiglione, prezzo_base)
                        self.stand.append(nuovo_stand)

                    if len(riga) == 5:

                        extra = riga[4].strip()

                            if extra.isdigit():
                                n_prese = int(extra)

                            else:

                                posizione = extra

        except FileNotFoundError:
            raise FileNotFoundError


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO

class Espositore:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome

    def __str__(self):

        return f"Codice: {self.codice} Nome: {self.nome} Cognome: {self.cognome}"

class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo_base, extra):
        self.codice = codice
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo_base = prezzo_base


    def __str__(self):

        return f"Codice: {self.codice} Sup: {self.superficie} Padiglione: {self.padiglione} Prezzo: {self.prezzo_base}")


class StandPreseExtra(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, n_prese):
        super.()__.init__(codice, superficie, padiglione, prezzo_base)

        self.n_prese = n_prese

class StandPremium(Stand):
    def __init__(selfself, codice, superficie, padiglione, prezzo_base, posizione):
        super()__.init__(codice, superficie, padiglione, prezzo_base)

        self.posizione = posizione


