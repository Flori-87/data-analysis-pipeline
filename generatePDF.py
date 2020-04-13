from fpdf import FPDF
import pandas as pd
from output import*
data = pd.read_csv("output/dataset_clean.csv")
data = data.drop(columns="Unnamed: 0")

def genPDF(region,income):
    arg_region = region
    arg_income = income

    dic_region = {"Sub-Saharan Africa":"SSA", "Western Europe":"WE", "Central and Eastern Europe":"CEE","Latin America and Caribbean":"LAC", 
    "Middle East and Northern Africa":"ENA", "Southeastern Asia":"SEA", "Southern Asia":"SA", "Eastern Asia":"EA", 
    "North America":"NA", "Australia and New Zealand":"ANZ"}

    for key in dic_region:
        if arg_region==key:
            region_mod = dic_region[key]

    pdf = FPDF("P","mm","A4")
    pdf.add_page()

    if arg_region == None and arg_income == None:
        pdf.image("output/graphs_no_params/table.png", x = 15, y = 15, w = 150, h = 120)
        pdf.image("output/graphs_no_params/precip.png", x = 15, y = 145, w = 100, h = 70)
        pdf.add_page()
        pdf.image("output/graphs_no_params/temp.png", x = 15, y = 225, w = 100, h = 70)

    elif arg_region == None:
        pdf.image(f"output/graphs_income/{arg_income}_table.png", x = 15, y = 15, w = 175, h = 70)
        pdf.image(f"output/graphs_income/{arg_income}.png", x = 15, y = 145, w = 95, h = 95)

    elif arg_income == None:
        pdf.image(f"output/graphs_region/{region_mod}_table.png", x = 15, y = 15, w = 180, h = 35)
        pdf.image(f"output/graphs_region/{region_mod}.png", x = 15, y = 145, w = 95, h = 95)
    
    else:
        data_region = data[data["Region"]==arg_region]
        income_list = list(data_region["Income"].value_counts().index)
        if arg_income in income_list:
            pdf.image(f"output/graphs_region_income/{region_mod}/{region_mod}_{arg_income}_table.png", x = 15, y = 15, w = 180, h = 25)
            pdf.image(f"output/graphs_region_income/{region_mod}/{region_mod}_{arg_income}.png", x = 15, y = 145, w = 95, h = 95)

    pdf.output("output/report.pdf","F")