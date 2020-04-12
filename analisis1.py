import pandas as pd

data = pd.read_csv("dataset_clean.csv")
data = data.drop(columns="Unnamed: 0")

# cuando se introduce uno o dos argumentos
def analisis(region,income):
    if income == None:
        data_analisis = data[data["Region"]==region]
    elif region == None:
        data_analisis = data[data["Income"]==income]
    else:
        lista_income = ["HIC","LIC","UMC","LMC"]
        if income in lista_income:
            data_region = data[data["Region"]==region] 
            incomes_region = list(data_region["Income"].value_counts().index)
            if income in incomes_region:
                data_analisis = data_region[data_region["Income"]==income]
            else:
                return "Sorry. There are not countries with that income in that region"
        else:
            return "Sorry. The value of income must be: HIC, LIC, UMC, LMC"
    data_group = data_analisis.groupby(["Region","Income"]).agg({"Rank":["min","max"],"Country":"count","Score":["min","max"],
                                                      "Economy":"max","Family":"max",
                                                      "Health":"max","Freedom":"max",
                                                      "Trust in Government":"max","Generosity":"max",
                                                       "Precip./month (mm)":"max","Temp. (ºC)":"max"})

    return data_group.sort_values(("Rank","min"))