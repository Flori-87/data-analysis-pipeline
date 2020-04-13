import pandas as pd
import numpy as np

data = pd.read_csv("output/dataset_clean.csv")
data = data.drop(columns="Unnamed: 0")
data_rank = data.set_index("Rank")

# Cuando no se introduce ningún argumento
def getSummary():
    lista_regiones= list(data_rank["Region"].value_counts().index)
    total = pd.DataFrame(columns = ["Rank","Region","Country","Score","Main contribution","Lower contribution", "Temp. (ºC)", "Precip./month (mm)"])
    for e in lista_regiones:
        data_region = data_rank[data_rank["Region"] == e]
        total = total.append({"Rank":getMin(data_region).index.values[0],"Region": e,
                              "Country":data_region["Country"][data_region["Country"].index == data_region.index.min()].values[0],
                              "Score":data_region["Score"][data_region["Country"]==data_region["Country"][data_region["Country"].index == data_region.index.min()].values[0]].values[0],
                              "Main contribution":getValueMax(getMin(data_region)),
                              "Lower contribution":getValueMin(getMin(data_region)),
                             "Temp. (ºC)":data_region["Temp. (ºC)"][data_region["Temp. (ºC)"].index == data_region.index.min()].values[0],
                             "Precip./month (mm)":data_region["Precip./month (mm)"][data_region["Precip./month (mm)"].index == data_region.index.min()].values[0]},
                             ignore_index=True)
        total = total.append({"Rank":getMax(data_region).index.values[0],"Region": e,
                              "Country":data_region["Country"][data_region["Country"].index == data_region.index.max()].values[0],
                              "Score":data_region["Score"][data_region["Country"]==data_region["Country"][data_region["Country"].index == data_region.index.max()].values[0]].values[0],
                              "Main contribution":getValueMax(getMax(data_region)),
                              "Lower contribution":getValueMin(getMax(data_region)),
                              "Temp. (ºC)":data_region["Temp. (ºC)"][data_region["Temp. (ºC)"].index == data_region.index.max()].values[0],
                             "Precip./month (mm)":data_region["Precip./month (mm)"][data_region["Precip./month (mm)"].index == data_region.index.max()].values[0]},
                              ignore_index=True)
    total = total.set_index(keys="Rank").sort_values("Rank")
    return total


def getMax(data_region):
    max_country=data_region[data_region.index == data_region.index.max()].drop(columns=['Score', 'Standard Error','Precip./month (mm)', 'Temp. (ºC)'])
    return max_country

def getMin(data_region):
    min_country=data_region[data_region.index == data_region.index.min()].drop(columns=['Score', 'Standard Error','Precip./month (mm)', 'Temp. (ºC)'])
    return min_country

def getValueMax(country):
    for e in country:
        if country[e].equals(country.max(axis=1,numeric_only=True)):
            return e
            #col_value = country[e].values[0]
    #return col
    
def getValueMin(country):
    for e in country:
        if country[e].equals(country.min(axis=1,numeric_only=True)):
            return e
            #col_value = country[e].values[0]
    #return col


# cuando se introduce uno o dos argumentos
def analisis(region,income):
    if checkParams(region,income)!=None:
        return checkParams(region,income)
    if checkParams(region,income)==None:
        if income == None:
            data_analisis = data[data["Region"]==region]
        elif region == None:
            data_analisis = data[data["Income"]==income]
        else:
            data_region = data[data["Region"]==region] 
            data_analisis = data_region[data_region["Income"]==income]
    data_group = data_analisis.groupby(["Region","Income"]).agg({"Rank":["min","max"],"Country":"count","Score":["min","max"],
                                                      "Economy":"max","Family":"max",
                                                      "Health":"max","Freedom":"max",
                                                      "Trust in Government":"max","Generosity":"max",
                                                       "Precip./month (mm)":"max","Temp. (ºC)":"max"})

    return data_group.sort_values(("Rank","min"))

def checkParams(region,income):
    if region!=None:
        regions_list = list(data["Region"].value_counts().index)
        if region not in regions_list:
            return "Sorry.The value of region must be: Sub-Saharan Africa, Central and Eastern Europe, Latin America and Caribbean, Western Europe, Middle East and Northern Africa, Southeastern Asia, Southern Asia, Eastern Asia, North America, Australia and New Zealand."
        elif income!=None:
            data_region = data[data["Region"]==region]
            income_list = list(data_region["Income"].value_counts().index)
            if income not in income_list:    
                return f"Sorry. There are not countries with that income in that region. Possible incomes are: {income_list}"
    elif region==None and income:
        total_income = ["HIC","LIC","UMC","LMC"]
        if income not in total_income:
            return f"Sorry. The value of income must be: {total_income}"
