#L4 - Create Python Console Application to read the contents of .json file and print in the VS Code python console output

import json 
f=open('C:/Users/kambl/OneDrive/Documents/PythonOverview/L4.json')

data = json.load(f)

for i in data['employee']:
    print(i)

f.close()    