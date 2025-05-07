Programa para graficar en barras el pace (ritmo) de una sesión de entrenamiento de carrera (trote) 
Versión 2.0

Inputs: Se debe ingresar el nombre del archivo CSV tipo "running_data_2.csv" extraido de COROS Training Hub (training.coros.com)

Se usa las librerías: pandas, matplotlib y numpy

Retos en esta versión 1.0:
- Transformar el pace que esta en string a int pero solo en segundos
- Calcular un pace inverso para poder graficar bien el ritmo
- Colocar el string de pace sobre cada barra
- Modificar el eje Y para poder visualizar el ritmo

Modificaciones de la versión 2.0:
- Ahora se debe ingresar el nombre del archivo csv a procesar
- Se crea un nuevo dataframe que consolide los laps: rapidos y lentos, esto sirve cuando no se configura la sesion bien desde el reloj
- el dataframe df3 suma la distancia de los laps, promedia el pace, y pone en string el pace, de los laps rapido y lentos
