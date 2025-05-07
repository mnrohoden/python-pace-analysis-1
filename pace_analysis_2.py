import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file into a DataFrame
filename = input("Ingresa el nombre del archivo CSV a analizar: ")
df = pd.read_csv(filename , usecols=['Split','Time','GetDistance','Avg Pace','Avg HR'])

# Se elimina la fjla del resumen de la actividad
df  = df.drop(len(df.index)-1)

# Quitar el 00: del pace y transformar el pace a segundos
pace_temp = []
pace_en_seg = []
for temp1 in df['Avg Pace']:
    temp2 = temp1.split(":")
    pace_temp.append(temp2[1] + ":" + temp2[2].strip()) # strip() le quita los espacios finales al pace
    pace_en_seg.append(int(temp2[1])*60 + int(temp2[2].strip()))

df['Avg Pace'] = pace_temp
df['Pace Seg'] = pace_en_seg

# Calcular datos para plotear mejor y se añade la columna Pace Inv
pace_max = 600 # el pace_max será de 600 (o 10min/km) para estandarizar el plot
print(pace_max)
pace_en_seg_inv = []
for i in df['Pace Seg']:
    if i > 600: i = 600 # no se ploteará pace mayor a 10min/km
    pace_en_seg_inv.append(pace_max - i)
df['Pace Inv'] =  pace_en_seg_inv

# Display the DataFrame
print (df)

# Crear nuevo dataframe con menos info para procesar
columns_to_remove = ['Time', 'Avg Pace', 'Avg HR', 'Pace Seg']
df2 = df.drop(columns=columns_to_remove)

# Crear nuevo dataframe que una los splits rapidos y lentos
df3 = pd.DataFrame(columns=['Split','GetDistance','Pace Inv'])
contador = 0
distancia = 0
pace = 0
rapido = True
indexador = 0
for index, row in df2.iterrows():
    if row['Pace Inv'] > 360: # Si el pace es mayor a 4min/km es rapido -> 240-600=360
        if rapido == False:
            df3.loc[indexador] = [indexador+1, distancia, pace/contador]
            indexador+=1
            rapido = True 
            contador = 0
            distancia = 0
            pace = 0
        contador+=1 
        distancia+=row['GetDistance']
        pace+=row['Pace Inv']
        rapido = True
    elif row['Pace Inv'] < 360:
        if rapido ==True:
            df3.loc[indexador] = [indexador+1, distancia, pace/contador]
            indexador+=1
            rapido = False 
            contador = 0
            distancia = 0
            pace = 0
        contador+=1 
        distancia+=row['GetDistance']
        pace+=row['Pace Inv']

# Para sacar el pace promedio en texto en formato min:seg
pace_promedio = []
for i in df3['Pace Inv']:
    pace_promedio.append(str(int((600-i)/60))+':'+(f"{int((600-i)%60):02d}"))
df3['Pace Prom'] =  pace_promedio
print(df3)

# Bar plot
widths = df3['GetDistance']
fig, ax = plt.subplots()
ax.bar(x = df3['Split'], height = df3['Pace Inv'], align ='center', color ="darkseagreen", width =widths)

# Se añade el texto para indicar el pace sobre la barra
for index, (value1, value2) in enumerate( zip (df3['Pace Inv'], df3['Pace Prom'])):
    plt.text(index+1, value1+10, str(value2), ha='center') # se añade espacio al texto para que se visualice mejor

plt.xlabel('Laps')
plt.ylabel('Pace (min/Km)')
plt.title('Pace Analysis')
# Se modifica el eje Y para mejor comprension del pace
plt.yticks(np.arange(0, 600, step=120), labels=['10','8','6','4','2'])
plt.show()
