from argparse import ArgumentParser
import pandas as pd
from src.analysis import *

parser = ArgumentParser(description="This program analyzes the World Happiness database")

parser.add_argument("--region",help="to analyze scores of countries in a world region", default=None)
parser.add_argument("--income",help="to analyze scores based on income", default=None)

args = parser.parse_args()
print(args)


if args.region==None and args.income==None:
    print(getSummary())
elif args.region or args.income:
    print(analisis(args.region,args.income))