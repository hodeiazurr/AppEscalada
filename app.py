import pandas as pd
import numpy as np


class Fuerza():
    def __init__(self, fuerza_agarre=0, fuerza_dedos=0, **kwargs):
        self.fuerza_agarre = fuerza_agarre
        self.fuerza_dedos = fuerza_dedos

    @property
    def fuerza_agarre(self):
        return self.__fuerza_agarre

    @fuerza_agarre.setter
    def fuerza_agarre(self, fuerza_agarre):
        self.__fuerza_agarre = fuerza_agarre

    @property
    def fuerza_dedos(self):
        return self.__fuerza_dedos

    @fuerza_dedos.setter
    def fuerza_dedos(self, fuerza_dedos):
        self.__fuerza_dedos = fuerza_dedos

    def fuerza_total(self):
        return (int(self.fuerza_dedos) + int(self.fuerza_agarre)) / 2

    def mostrar(self):
        return f"fuerza dedos: {self.fuerza_dedos}, fuerza agarre: {self.fuerza_agarre}"


class Resistencia():
    def __init__(self, resistencia_aerobica=0, resistencia_anaerobica=0, **kwargs):
        self.resistencia_aerobica = resistencia_aerobica
        self.resistencia_anaerobica = resistencia_anaerobica

    @property
    def resistencia_aerobica(self):
        return self.__resistencia_aerobica

    @resistencia_aerobica.setter
    def resistencia_aerobica(self, resistencia_aerobica):
        try:
            self.__resistencia_aerobica = float(resistencia_aerobica)
        except ValueError:
            raise ValueError("La resistencia aeróbica debe ser un valor numérico")

    @property
    def resistencia_anaerobica(self):
        return self.__resistencia_anaerobica

    @resistencia_anaerobica.setter
    def resistencia_anaerobica(self, resistencia_anaerobica):
        try:
            self.__resistencia_anaerobica = float(resistencia_anaerobica)
        except ValueError:
            raise ValueError("La resistencia anaeróbica debe ser un valor numérico")

    def resistencia_total(self):
        return (self.resistencia_aerobica + self.resistencia_anaerobica) / 2

    def mostrar(self):
        return f"resistencia aeróbica: {self.resistencia_aerobica}, resistencia anaeróbica: {self.resistencia_anaerobica}"


class Escalada(Fuerza, Resistencia):
    def __init__(self, persona, fuerza_agarre, fuerza_dedos, resistencia_aerobica, resistencia_anaerobica, edad=0,
                 **kwargs):
        super().__init__(fuerza_agarre=fuerza_agarre, fuerza_dedos=fuerza_dedos, **kwargs)
        Resistencia.__init__(self, resistencia_aerobica=resistencia_aerobica,
                             resistencia_anaerobica=resistencia_anaerobica, **kwargs)

        self.persona = persona
        self.edad = edad
        self.nivel = kwargs.get('nivel', '5a')
        self.preferencia = kwargs.get('preferencia', 'mixto')

    @property
    def persona(self):
        return self.__persona

    @persona.setter
    def persona(self, persona):
        self.__persona = persona

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    def edad_valido(self):
        return self.__edad >= 18

    def entrenamiento(self):
        if self.edad_valido():
            if 0 <= self.fuerza_total() <= 33 and 0 <= self.resistencia_total() <= 33:
                return f"2 días de gimnasio y 1 día de bulder, otro de escalada deportiva y los restantes {self.preferencia}"
            elif 33 < self.fuerza_total() <= 66 and 0 <= self.resistencia_total() <= 33:
                return "2 días gimnasio y 3 días rocodromo y un día de escalada deportiva"
            elif 66 < self.fuerza_total() <= 100 and 0 <= self.resistencia_total() <= 33:
                return f"1 día gimnasio, 2 días de bulder y 3 días de escalada deportiva grado: {self.nivel}"
            elif 0 <= self.fuerza_total() <= 33 and 33 < self.resistencia_total() <= 66:
                return "3 días de gimnasio, 2 días de bulder y uno de escalada deportiva"
            elif 33 < self.fuerza_total() <= 66 and 33 < self.resistencia_total() <= 66:
                return f"2 días de gimnasio, 1 día de bulder y 2 días de escalada deportiva grado {self.nivel}"
            elif 66 < self.fuerza_total() <= 100 and 33 < self.resistencia_total() <= 66:
                return f"1 día de gimnasio, 3 días de bulder grado: {self.nivel} y 2 de escalada deportiva"
            elif 0 <= self.fuerza_total() <= 33 and 66 < self.resistencia_total() <= 100:
                return f"3 días de gimnasio y 3 días de bulder grado: {self.nivel}"
            elif 33 < self.fuerza_total() <= 66 and 66 < self.resistencia_total() <= 100:
                return f"3 días de gimnasio, 2 días de bulder y uno de escalada deportiva en ambos en grado: {self.nivel}"
            elif 66 <= self.fuerza_total() <= 100 and 66 < self.resistencia_total() <= 100:
                return f"1 día bulder, 1 día gimnasio y otro día de escalada deportiva. Días restantes: {self.preferencia}, nivel: {self.nivel}"
        else:
            return "Se recomienda que sea mayor de edad para realizar un entrenamiento"


def tabla():
    nombre = []
    edad = []
    nivel = []
    preferencia = []

    try:
        index = int(input("¿Cuántas personas quieren preparar un entrenamiento? "))
    except ValueError:
        print("Debe ser un valor numérico")
        index = 0

    for i in range(index):
        nom = input(f"Nombre de la persona {i + 1}: ")
        try:
            ed = int(input(f"Edad de la persona {i + 1}: "))
        except ValueError:
            print("La edad debe ser un valor numérico")
            ed = 0
        niv = input(f"Grado de escalada de la persona {i + 1} (ejemplo: 6b): ")
        pref = input(f"Preferencia de la persona {i + 1} (bulder/escalada deportiva/mixto): ")

        nombre.append(nom)
        edad.append(ed)
        nivel.append(niv)
        preferencia.append(pref)

    fuerza_dedos = np.random.randint(0, 101, index)
    fuerza_agarre = np.random.randint(0, 101, index)
    resistencia_aerobica = np.random.randint(0, 101, index)
    resistencia_anaerobica = np.random.randint(0, 101, index)

    df = pd.DataFrame({
        'Nombre': nombre,
        'Edad': edad,
        'Fuerza_Dedos': fuerza_dedos,
        'Fuerza_Agarre': fuerza_agarre,
        'Resistencia_Aerobica': resistencia_aerobica,
        'Resistencia_Anaerobica': resistencia_anaerobica,
        'Nivel': nivel,
        'Preferencia': preferencia
    })
    return df


if __name__ == "__main__":
    datos = tabla()
    for j in range(len(datos)):
        escalada = Escalada(
            persona=datos['Nombre'][j],
            edad=datos['Edad'][j],
            fuerza_dedos=datos['Fuerza_Dedos'][j],
            fuerza_agarre=datos['Fuerza_Agarre'][j],
            resistencia_aerobica=datos['Resistencia_Aerobica'][j],
            resistencia_anaerobica=datos['Resistencia_Anaerobica'][j],
            nivel=datos['Nivel'][j],
            preferencia=datos['Preferencia'][j]
        )
        if datos['Edad'][j] >= 18:
            print(f"El entrenamiento para {escalada.persona} sería: {escalada.entrenamiento()} / por semana \n"
                  f"Fuerza: {escalada.fuerza_total()}, Resistencia: {escalada.resistencia_total()}")
        else:
            print(f"En el caso de {escalada.persona}: {escalada.entrenamiento()}")
