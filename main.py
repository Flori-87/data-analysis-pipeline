from argparse import ArgumentParser
import os 
import sys
module_path = os.path.abspath(os.path.join('funciones.py'))
if module_path not in sys.path:
    sys.path.append(module_path)
from analisis1 import *
from analisis2 import *


parser = ArgumentParser(description="This program analyzes the World Happiness database")

parser.add_argument("--region",help="to analyze scores of countries in a world region", default=None)
parser.add_argument("--income",help="to analyze scores based on income", default=None)
#parser.add_argument("--times",help="veces que saludar", default=1, type=int)
#parser.add_argument("--say",help="dilo en voz alta", action='store_true')

args = parser.parse_args()
print(args)


if args.region==None and args.income==None:
    print(getSummary())
elif args.region or args.income:
    print(analisis(args.region,args.income))