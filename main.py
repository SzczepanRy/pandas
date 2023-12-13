import pandas as pd
import numpy as np
import urllib3

urllib3.disable_warnings()

main = pd.read_excel("./Zeszyt1.xlsx", sheet_name=None)

print(main.keys())
keys =[]

currentKeys=[]
data = {}


l1 = []
for dfname in main.keys():

    df = main[dfname]
    for index, row in df.iterrows():
        l1.append(row.to_list())

print(l1)
for arr in l1:
    for value in arr:
        # print(value)
        if(type(value) is str):
            if(value not in data.keys()):
                keys.append(value)      
                

dfnames=[]
for dfname in main.keys():
    dfnames.append(dfname)

data["Tables"] = dfnames
for key in keys :
    data[key] = list(np.zeros(len(main.keys()), dtype=int))

print(l1)

keys =[]
i= 0
for dfname in main.keys():

    df = main[dfname]
    for index, row in df.iterrows():
        row.to_list()
        currentKey=""
        for value in row:
            # print(value)
        
        
            if(type(value) is str):
                currentKey=value
                # print("string")
                # if(value not in data.keys()):
                #     keys.append(value)
                #     # for key in main.keys():
                #     #     data[value].append(0)
                

            if(type(value) is int ):
                print(value)
                
                # for key in keys :
                print(data[currentKey])
                data[currentKey][i] =  value 
    i+=1
                     
         


print(keys)

print(data)
dataFrame = pd.DataFrame.from_dict(data, orient='index')
dataFrame = dataFrame.transpose()
# Export the DataFrame to an Excel file
dataFrame.to_excel('output.xlsx', index=False)
#df.to_excel("")
