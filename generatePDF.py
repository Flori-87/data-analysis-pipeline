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
    pdf.set_font("Arial", "B", 12)

    if arg_region == None and arg_income == None:
        pdf.text(15,15,f"World Happiness analysis by the happiest and lowest happy countries in each region")
        pdf.image("output/graphs_no_params/table.png", x = 15, y = 30, w = 150, h = 120)
        pdf.set_font("Arial",size=9)
        pdf.text(15,160,f"This table shows the first and last countries in the ranking per region. The topics that contribute the most ")
        pdf.text(15,164,"and least to their happiness are presented.")
        pdf.image("output/graphs_no_params/precip.png", x = 15, y = 185, w = 100, h = 70)
        pdf.text(15,258,f"The bar graph shows the precipitation level average per month (mm) by country.")
        pdf.add_page()
        pdf.image("output/graphs_no_params/temp.png", x = 15, y = 15, w = 100, h = 70)
        pdf.text(15,90,f"The bar graph shows the temperature average (ºC) by country.")
        pdf.set_font("Arial",style="B",size=10)
        pdf.text(15,115,f"Conclusion. There is no correlation between weather and happiness. However, economy is the main ") 
        pdf.text(15,120,"factor impacting in happiness.")

    elif arg_region == None:
        dict_incomes = {"HIC":"high","UMC":"upper-middle","LMC":"low-middle","LIC":"low"}
        for key in dict_incomes:
            if arg_income==key:
                title_income = dict_incomes[key]
        pdf.text(15,15,f"World Happiness analysis by {title_income} income in each region")
        pdf.image(f"output/graphs_income/{arg_income}_table.png", x = 15, y = 25, w = 175, h = 70)
        pdf.set_font("Arial",size=9)
        pdf.text(15,110,f"This table shows the maximum scores for the analyzed topics in countries with {title_income} income.")
        pdf.image(f"output/graphs_income/{arg_income}.png", x = 15, y = 135, w = 95, h = 95)
        pdf.text(15,240,f"The bar graph shows the lowest and highest happiness scores in each region.")

    elif arg_income == None:
        pdf.text(15,15,f"World Happiness analysis by incomes in {arg_region} region")
        pdf.image(f"output/graphs_region/{region_mod}_table.png", x = 15, y = 25, w = 180, h = 35)
        pdf.set_font("Arial",size=9)
        pdf.text(15,74,f"This table shows the first and last countries in the ranking based on their incomes and the maximum scores for the analyzed ")
        pdf.text(15,78,f"topics in {arg_region} region.")
        pdf.image(f"output/graphs_region/{region_mod}.png", x = 15, y = 105, w = 95, h = 95)
        pdf.text(15,210,f"The bar graph shows the maximum scores for the analyzed topics by incomes.")
    
    else:
        data_region = data[data["Region"]==arg_region]
        income_list = list(data_region["Income"].value_counts().index)
        if arg_income in income_list:
            dict_incomes = {"HIC":"high","UMC":"upper-middle","LMC":"low-middle","LIC":"low"}
            for key in dict_incomes:
                if arg_income==key:
                    title_income = dict_incomes[key]
            pdf.text(15,15,f"World Happiness analysis by {title_income} income in {arg_region} region")
            pdf.image(f"output/graphs_region_income/{region_mod}/{region_mod}_{arg_income}_table.png", x = 15, y = 30, w = 180, h = 25)
            pdf.set_font("Arial",size=9)
            pdf.text(15,74,f"This table shows the first and last countries with a {title_income} income and the maximum scores for the analyzed topics")
            pdf.text(15,78,f"in {arg_region} region.")
            pdf.image(f"output/graphs_region_income/{region_mod}/{region_mod}_{arg_income}.png", x = 15, y = 125, w = 95, h = 95)
            pdf.text(15,230,f"The bar graph shows the maximum scores for the analyzed topics in the countries in {arg_region} region")
            pdf.text(15,234,f"with a {title_income} income.")

    pdf.output("output/report.pdf","F")