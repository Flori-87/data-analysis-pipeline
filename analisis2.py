import pandas as pd

data = pd.read_csv("dataset_clean.csv")
data = data.drop(columns="Unnamed: 0")
data = data.set_index("Rank")

# Cuando no se introduce ningún argumento
def getSummary():
    lista_regiones= list(data["Region"].value_counts().index)
    total = pd.DataFrame(columns = ["Rank","Region","Country","Score","Main contribution","Lower contribution", "Temp. (ºC)", "Precip./month (mm)"])
    for e in lista_regiones:
        data_region = data[data["Region"] == e]
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