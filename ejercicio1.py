class Fecha:
    def __init__(self, dd, mm, aaaa):
        self.dd = dd
        self.mm = mm
        self.aaaa = aaaa
    def __str__(self):
        return f"{self.dd}/{self.mm}/{self.aaaa}"

    def __add__(self, other):
        dias = self.dd + other.dd
        meses = self.mm + other.mm
        anios = self.aaaa + other.aaaa
        return Fecha(dias, meses, anios)

    def __eq__(self, other):
        return self.dd == other.dd and self.mm == other.mm and self.aaaa == other.aaaa

    def calcular_dif_fecha(self, other):
        dias = abs(self.dd - other.dd)
        meses = abs(self.mm - other.mm)
        anios = abs(self.aaaa - other.aaaa)
        return f"{dias} dias, {meses} meses y {anios} años"


