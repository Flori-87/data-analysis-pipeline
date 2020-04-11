import os 
import sys
from argparse import ArgumentParser
import pandas as pd
import subprocess

data = pd.read_csv("dataset_clean.csv")
"""
def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])
    #return proc.stdout.read()
"""
def analisis(region):
    
    return data[data["Region"] == region].describe





parser = ArgumentParser(description="Este programa es para obtener scores de felicidad")

parser.add_argument("--region",help="la region a analizar", default="Western Europe")
#parser.add_argument("--lugar",help="desde donde saludar", default="la playa")
#parser.add_argument("--times",help="veces que saludar", default=1, type=int)
#parser.add_argument("--say",help="dilo en voz alta", action='store_true')

args = parser.parse_args()
print(args)

if args.region:
    print(analisis(args.region))


"""
result = []
for i in range(args.times):
    result.append(saluda(args.lang,args.lugar))

saludototal = '\n'.join(result)
if args.say:
    print(saludototal)
    voices = ["Alex","Amelie","Fiona","Kyoko","Luciana","Monica"]
    selected_voice = random.choice(voices)

    print(f"Now the voice of {selected_voice}!")
    cmd = f"say -v '{selected_voice}' '{saludototal}'"
    print(cmd)
    bash_command(cmd)
else:
    print(saludototal)
"""