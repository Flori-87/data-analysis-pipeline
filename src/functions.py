# Functions to get APIs info
import requests
import statistics as st

def getIncome(ISO):
    url = f"http://api.worldbank.org/v2/country/{ISO}?format=json"
    res = requests.get(url)
    #print(res)
    res_income = res.json()
    return res_income[1][0]["incomeLevel"]["id"]


def getPrecip(ISO):
    url = f"http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/pr/year/{ISO}"
    res = requests.get(url)
    #print(res)
    res_precip = (res.json())[-5:]
    precip=[]
    for i in range(len(res_precip)):
        precip.append(res_precip[i]["data"])
    media = round(st.mean(precip),2)
    #st_dev = round(st.pstdev(precip),2)
    return media

def getTemp(ISO):
    url = f"http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/year/{ISO}"
    res = requests.get(url)
    #print(res)
    res_temp = (res.json())[-5:]
    temp=[]
    for i in range(len(res_temp)):
        temp.append(res_temp[i]["data"])
    media = round(st.mean(temp),2)
    #st_dev = round(st.pstdev(temp),2)
    return media