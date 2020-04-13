from argparse import ArgumentParser
import pandas as pd
from src.analysis import *

def programHappiness(region,income):
    if args.region==None and args.income==None:
        print("This table shows a summary with the happiest and least happy country in each region.")
        print(getSummary())
    
    elif args.region or args.income:
        print(analisis(args.region,args.income))


parser = ArgumentParser(description="This program analyzes the World Happiness database")
parser.add_argument("--region",help="to analyze scores of countries in a world region", default=None)
parser.add_argument("--income",help="to analyze scores based on income", default=None)

args = parser.parse_args()
print(args)

if __name__ == "__main__":
    programHappiness(args.region,args.income)