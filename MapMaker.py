# by YiBin, Guo
import pandas as pd


schools = pd.read_excel(r'data.xlsx', sheet_name=1)
schoolName = schools['Institution'].values
schoolGeo = schools['Address'].values
PIName = schools['PI'].values

print(schoolName, schoolGeo, PIName)


replaceScatterGeo = ''
for i in range(len(schoolName)):
    s = '"{}":[{:.2f}, {:.2f}],'.format(schoolName[i], float(schoolGeo[i].split(',')[0]), float(schoolGeo[i].split(',')[1]))
    print(s)
    replaceScatterGeo += s

replaceScatterVal= ''
for i in range(len(schoolName)):
    print(PIName[i])
    names = PIName[i].split(',')
    names_str = ''
    for name in names:
        names_str += '<br>' 
        names_str += str(name) 
    s = '{{name:"{}", value:"{}"}},'.format(schoolName[i],names_str)
    print(s)
    replaceScatterVal += s


a = open('index.html', 'r', encoding='utf-8')
string = a.read()

string = string.replace('replaceScatterGeo', replaceScatterGeo)
string = string.replace('replaceScatterVal', replaceScatterVal)

b = open(r'quantum_map.html', 'w', encoding= 'utf-8')
b.write(string)
b.close()

