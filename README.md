# Entrenamiento de Escalada

## Descripción

Esta aplicación genera un plan de entrenamiento personalizado para escaladores basado en su nivel de fuerza y resistencia. Utiliza datos aleatorios para las pruebas físicas, tales como fuerza de agarre, fuerza de los dedos, resistencia aeróbica y anaeróbica, y sugiere un entrenamiento semanal personalizado. Los planes varían dependiendo de la edad, nivel de escalada y preferencias del usuario.

## Funcionalidades

- Introducir datos de varias personas para calcular sus entrenamientos personalizados.
- Generar entrenamientos semanales basados en el nivel de fuerza y resistencia.
- Soporta diferentes tipos de escalada: boulder, escalada deportiva, o mixto.
- Usa herencia de clases para modelar características físicas y recomendaciones.
- Maneja excepciones en caso de entradas incorrectas de datos.

## Requisitos

- Python 3.x
- Librerías necesarias:
  - `pandas`
  - `numpy`


## Clases

### 1. Fuerza

La clase `Fuerza` representa la fuerza de un escalador, dividiéndose en dos componentes: fuerza de agarre y fuerza de dedos.

#### Atributos

- `fuerza_agarre` (int): Fuerza de agarre del escalador.
- `fuerza_dedos` (int): Fuerza de los dedos del escalador.

#### Métodos

- `fuerza_total()`: Calcula la fuerza total como el promedio de la fuerza de agarre y la fuerza de dedos.
- `mostrar()`: Retorna una cadena con la información de la fuerza de dedos y de agarre.

### 2. Resistencia

La clase `Resistencia` representa la resistencia aeróbica y anaeróbica de un escalador.

#### Atributos

- `resistencia_aerobica` (float): Resistencia aeróbica del escalador.
- `resistencia_anaerobica` (float): Resistencia anaeróbica del escalador.

#### Métodos

- `resistencia_total()`: Calcula la resistencia total como el promedio de la resistencia aeróbica y anaeróbica.
- `mostrar()`: Retorna una cadena con la información de la resistencia aeróbica y anaeróbica.

### 3. Escalada

La clase `Escalada` hereda de `Fuerza` y `Resistencia`, integrando las características de ambas clases para crear un modelo de escalador completo.

#### Atributos

- `persona` (str): Nombre de la persona.
- `edad` (int): Edad de la persona.
- `nivel` (str): Nivel de escalada (por ejemplo, "5a"). Se podría agregar más de un nivel.
- `preferencia` (str): Preferencia de entrenamiento (bulder/escalada deportiva/mixto). Se podría agregar más de una preferencia.

#### Métodos

- `edad_valido()`: Verifica si la edad es válida (mayor o igual a 18 años).
- `entrenamiento()`: Retorna un plan de entrenamiento basado en la fuerza total, resistencia total y edad del escalador.

### 4. Función `tabla()`

La función `tabla()` recopila información de múltiples escaladores y genera un `DataFrame` de pandas con sus datos, como nombre, edad, fuerza de dedos, fuerza de agarre, resistencia aeróbica, resistencia anaeróbica, nivel y preferencia de entrenamiento.

## Uso

Al ejecutar el script, se solicita al usuario la información de varias personas interesadas en el entrenamiento de escalada. Luego, se crean instancias de la clase `Escalada` para cada persona y se imprime el plan de entrenamiento correspondiente, basado en sus características individuales.

```python
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

