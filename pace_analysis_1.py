import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file into a DataFrame
filename = "running_data_1.csv"
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
pace_max = df['Pace Seg'].max() + 60

pace_en_seg_inv = []
for i in df['Pace Seg']:
    pace_en_seg_inv.append(pace_max - i)
df['Pace Inv'] =  pace_en_seg_inv

# Display the DataFrame
print (df)


# Bar plot
widths = df['GetDistance']
fig, ax = plt.subplots()
ax.bar(x = df['Split'], height = df['Pace Inv'], align ='center', color ="darkseagreen", width =widths)

# Se añade el texto para indicar el pace sobre la barra
for index, (value1, value2) in enumerate( zip (df['Pace Inv'], df['Avg Pace'])):
    plt.text(index, value1+10, str(value2), ha='center') # se añade espacio al texto para que se visualice mejor

plt.xlabel('Laps')
plt.ylabel('Pace (min/Km)')
plt.title('Pace Analysis')
# Se modifica el eje Y para mejor comprension del pace
plt.yticks(np.arange(0, 600, step=120), labels=['10','8','6','4','2'])
plt.show()


