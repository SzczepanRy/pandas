
# worldAssemblyPartNumber

import requests
import json
import pandas as pd


initNames =["NU215","NU218","NU220","NU2224","NU2224" ,"NU224","NU2317","NU309",
"NU311",
"NU315",
"NU316",
"NU318",
"NU318C3",
"NU319",
"NU320",
"NU322",
"NU324",
"NU324C3",
"NU326C3"]



url = "https://engineering.timken.com/wp-json/timken-api/v1/BearingSearchAPI/FetchBearingProductData"


names = []

data={ }

titles=[]

for initName in initNames:
        
    payload = json.dumps({
    "pageNumber": 1,
    "rowsOfPage": 5,
    "unit": "M",
    "marketPlaceDescription": initName
    })
    headers = {
    'authority': 'engineering.timken.com',
    'accept': 'application/json',
    'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://engineering.timken.com',
    'referer': 'https://engineering.timken.com/engineering-tool/bearing-periodic-frequencies/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'x-gigya-jwt-sig': 'null'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    dataJson = response.json()

    arrJson = dataJson['bearingInformation']
    for obj in arrJson:
        names.append(obj["worldAssemblyPartNumber"])

names = list(set(names))


data["names"] = names

url = "https://engineering.timken.com/wp-json/timken-api/v1/PeriodicFrequencyAPI/CalcPerFreqWithCoefficients"


for name in names:
        

    payload = json.dumps({
    "partNumberOrWorldPartNumber": name,
    "cupPartNumber": "",
    "bearingType": "CRB",
    "bearingSubType": "1ROW",
    "units": "M",
    "operatingSpeed": 60,
    "rotationSpeed": [
        "60"
    ],
    "isDBRetrieval": True,
    "isReportRequired": True
    })
    headers = {
    'authority': 'engineering.timken.com',
    'accept': 'application/json',
    'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://engineering.timken.com',
    'referer': 'https://engineering.timken.com/engineering-tool/bearing-periodic-frequencies/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    resJson = response.json()
    resArr = resJson["report"]
#name : val
    for obj in resArr:
        dataArr = obj["data"]
        
        tempArr =[]
        for objData in dataArr:
            for el in objData["sectionData"]:
                if((el[0]+"("+el[2]+")") in data.keys()):
                    data[el[0]+"("+el[2]+")"].append(el[1])
                else:
                    data[el[0]+"("+el[2]+")"] = [el[1]]

            
           

        # data[name] = tempArr


print(data)
# print(titles)
# print(tempArr)



dataFrame = pd.DataFrame.from_dict(data, orient='index')
dataFrame = dataFrame.transpose()

dataFrame.to_excel('output2.xlsx', index=False)