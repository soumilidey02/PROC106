import plotly.express as px
import csv
import numpy as n

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Coffee in ml", y="sleep in hours")
        fig.show()

def getDataSource(data_path):
    sleep = []
    coffee= []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sleep.append(float(row["Sleep in Hours"]))
            coffee.append(float(row["Coffee in ml"]))

    return {"x" : sleep, "y": coffee}

def findCorrelation(datasource):
    correlation = n.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between the amount of coffee consumed and sleep:-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data/data1.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()
