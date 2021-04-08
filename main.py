# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from os import listdir
import matplotlib.pyplot as plt
import seaborn as sns

from os.path import isfile, join
import csv
from datetime import datetime


import pandas as pd
'''
    obiettivi:

    1) generare csv sha || family || tempo FATTO
    2) diagramma a torta famiglie FATTO
    3) istogramma temporale FATTO
    4) boxplot categorie opcode FATTO

'''
def countFamily():
    f = open("familyCount.txt", "a")

    for x in shacfglist:
        if shafamilydict[x] not in familycount.keys():
            familycount[shafamilydict[x] ]=1
        else:
            familycount[shafamilydict[x] ]=familycount[shafamilydict[x] ]+1
    for x in familycount.keys():
        f.write(str(x) + "=" + str(familycount[x]))
        f.write("\n")


def GeneraCSV():
    # generazione del csv
    with open('sha-family.csv', mode='a') as csv_file:
        fieldnames = ['Sha', 'Family','Time']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for x in shacfglist:
            writer.writerow({'Sha': str(x), 'Family': str(shafamilydict[str(x)]),"Time": str(shatimedict[str(x)])})


def GeneraDate():
    mesi2020 = dict()
    mesi2021 = dict()

    for i in range(1,13):
        mesi2020[i]=0
        mesi2021[i]=0

    # date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

    for x in shacfglist:

        datastring = shatimedict[x]

        #print(datastring)

        data = datetime.strptime(datastring, '%Y-%m-%d %H:%M:%S')

        if data.year == 2020:
            mesi2020[data.month]=mesi2020[data.month]+1
        elif data.year ==2021:
            mesi2021[data.month]=mesi2021[data.month]+1
        else:
            print("ERRORE "+str(data.year))
    f = open("datacount.txt", "a")

    for x in mesi2020.keys():
        f.write(str(x)+" : "+str(mesi2020[x]))
        f.write("\n")
    for y in mesi2021.keys():
        f.write(str(y)+" : "+str(mesi2021[y]))
        f.write("\n")
    f.close()

def generaFileBoxPlot():
    output = open("BOXPLOT.txt","a")
    output.write("numero_totale"+","+"categorie\n")

    report = open("/home/kali/PycharmProjects/StatisticGenerator/MagicReportCOPY.txt","r")
    linee = report.readlines()

    for l in linee:

        array = list()

        for i in l.split(","):
            array.append(i)


        output.write(str(array[0].replace("[",""))+',"C1"')
        output.write("\n")

        output.write(str(array[1].replace(" ",""))+',"C2"')
        output.write("\n")

        output.write(str(array[2].replace(" ",""))+',"C3"')
        output.write("\n")

        output.write(str(array[3].replace(" ",""))+',"C4"')
        output.write("\n")

        output.write(str(array[4].replace(" ",""))+',"C5"')
        output.write("\n")

        output.write(str(array[5].replace(" ",""))+',"C6"')
        output.write("\n")

        output.write(str(array[6].replace(" ",""))+',"C7"')
        output.write("\n")

        output.write(str(array[7].replace(" ",""))+',"C8"')
        output.write("\n")

        output.write(str(array[8].replace("]","").replace("\n","").replace(" ",""))+',"C9"')
        output.write("\n")
    report = open("/home/kali/PycharmProjects/StatisticGenerator/Statistiche/MagicReportAntonella.txt", "r")
    linee = report.readlines()

    for l in linee:

        array = list()

        for i in l.split(","):
            array.append(i)

        output.write(str(array[0].replace("[", "")) + ',"C1"')
        output.write("\n")

        output.write(str(array[1].replace(" ", "")) + ',"C2"')
        output.write("\n")

        output.write(str(array[2].replace(" ", "")) + ',"C3"')
        output.write("\n")

        output.write(str(array[3].replace(" ", "")) + ',"C4"')
        output.write("\n")

        output.write(str(array[4].replace(" ", "")) + ',"C5"')
        output.write("\n")

        output.write(str(array[5].replace(" ", "")) + ',"C6"')
        output.write("\n")

        output.write(str(array[6].replace(" ", "")) + ',"C7"')
        output.write("\n")

        output.write(str(array[7].replace(" ", "")) + ',"C8"')
        output.write("\n")

        output.write(str(array[8].replace("]", "").replace("\n", "").replace(" ", "")) + ',"C9"')
        output.write("\n")
    report = open("/home/kali/PycharmProjects/StatisticGenerator/Statistiche/magicCarlo.txt", "r")
    linee = report.readlines()

    for l in linee:

        array = list()

        for i in l.split(","):
            array.append(i)

        output.write(str(array[0].replace("[", "")) + ',"C1"')
        output.write("\n")

        output.write(str(array[1].replace(" ", "")) + ',"C2"')
        output.write("\n")

        output.write(str(array[2].replace(" ", "")) + ',"C3"')
        output.write("\n")

        output.write(str(array[3].replace(" ", "")) + ',"C4"')
        output.write("\n")

        output.write(str(array[4].replace(" ", "")) + ',"C5"')
        output.write("\n")

        output.write(str(array[5].replace(" ", "")) + ',"C6"')
        output.write("\n")

        output.write(str(array[6].replace(" ", "")) + ',"C7"')
        output.write("\n")

        output.write(str(array[7].replace(" ", "")) + ',"C8"')
        output.write("\n")

        output.write(str(array[8].replace("]", "").replace("\n", "").replace(" ", "")) + ',"C9"')
        output.write("\n")


def generaBlox():
    read_file = pd.read_csv(r'BOXPLOT.txt')
    read_file.to_csv(r'BOXPLOT.csv', index=None)

    sns.set_theme(style="whitegrid")
    prova = pd.read_csv("BOXPLOT.csv", sep=",")
    # ax = sns.boxplot(x=tips["total_bill"])
    ax = sns.boxplot(x="categorie", y="numero_totale", data=prova, palette="Reds")
    # ax = sns.boxplot(x=prova["categorie"], y=prova["numero_totale"])

    plt.show()




colnames = ['a','b','c','d','e','f','g','h','i','l','m','n','o','p' ]

data = pd.read_csv('/home/kali/PycharmProjects/StatisticGenerator/full.csv',names=colnames)

#shalist = data.b.tolist()
shacode = data.b.tolist()
timescol = data.a.tolist()
familycol = data.i.tolist()

shaposdict = dict()
shafamilydict=dict()
shatimedict = dict()

familycount =dict() #chiave = famiglia, valore = amount




i = 0

#f = open("sha.txt", "a")


for s in shacode:

    '''
        if i ==3 :
        break
    print(s)
    print(x)
    '''

    x = str(s).replace('"',"")
    x = x.replace(" ","")
    '''
    f.write(x)
    f.write("\n")
    '''


    shaposdict[x]=i
    shafamilydict[x]=familycol[i]
    shatimedict[x]=timescol[i]

    i = i+1



#f.close()

#print(str(shacode[7])+" : "+str(shafamilydict[shacode[7]]))





#metti qui il tuo indirizzo dei csv generati
csvlocator = "/home/kali/PycharmProjects/CFGGenerator/assemblyMalware"



Cvslist = [f for f in listdir(csvlocator) if isfile(join(csvlocator, f))]

shacfglist = list()

f = open("shaCFG.txt", "a")


for m in Cvslist:

    sha = m.split('.')[0]
    shacfglist.append(str(sha))

    f.write(str(sha))
    f.write("\n")

print("per ora ho "+str(len(shacfglist)))


a = open ("/home/kali/PycharmProjects/StatisticGenerator/Statistiche/ListHashAntonella.txt")


for x in a.readlines():
    shacfglist.append(x.replace("\n",""))
    f.write(str(x.replace("\n","")))
    f.write("\n")

print("ora ho "+str(len(shacfglist)))

c = open ("/home/kali/PycharmProjects/StatisticGenerator/Statistiche/hash_nameCarlo.txt")

for y in c.readlines():
    #shacfglist.append(y.replace("\n",""))
    f.write(str(y.replace("\n", "")))
    f.write("\n")

print("NUM MALWARE TOTALE  "+str(len(shacfglist)))


err = 0
try:
    countFamily()
    GeneraCSV()
    GeneraDate()

    generaFileBoxPlot()
    generaBlox()
except Exception as e:
    print(e)
    err = err + 1

print("errori totali = "+str(err))

'''


'''

'''
def getFamily(sha):
    return shafamily[shapos[sha]]
    def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


'''


