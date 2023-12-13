import pandas as pd

import urllib3

urllib3.disable_warnings()

main = pd.read_excel("./Zeszyt1.xlsx", sheet_name=None)
# df = pd.read_excel("./tee.xlsx")
print(main.keys())
keys =["column"]

currentKeys=[]
data = [{"column":[12,3,3,4]}]

for dfname in main.keys():

    df = main[dfname]

    print(df)
    names = df.iloc[:, 0].tolist()
    # print(names)

    print(names)


    currentKeys=[]
 

    for name in names :
        if(name in keys):
            for obj in data:
                print(obj)
                currentKeys.append(name)

        else:
            keys.append(name)
            currentKeys.append(name)
            data.append({name:[]})
    print("--------------------")
    print(currentKeys)


    for i in range(1,int(len(df.columns)+1)):
        # print(i)
        if(i<len(df.columns)):
            column = df.iloc[:, i].tolist()
        print("##################")
        print(column)
        # for value in column:

        print(currentKeys[i-1])# nazwa
        for obj in data:
            if(list(obj.keys())[0] == list(set(currentKeys))[i-1]):
                obj[list(set(currentKeys))[i-1]].append(column[i-1])
    
                

print("##################")
print(keys)
print(currentKeys)
print(data)
print("##################")
print(len(df.columns))
# print(names)

objData = {}
for obj in data:
    key = list(obj.keys())[0]
    objData[key] = obj[key]
print(objData)


dataFrame = pd.DataFrame.from_dict(objData, orient='index')
dataFrame = dataFrame.transpose()
# Export the DataFrame to an Excel file
dataFrame.to_excel('output.xlsx', index=False)
#df.to_excel("")
