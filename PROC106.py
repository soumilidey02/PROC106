import plotly.express as px
import csv
import numpy as n

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Days Present", y="Marks In Percentage")
        fig.show()

def getDataSource(data_path):
    marksInPercentage = []
    daysPresent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marksInPercentage.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))

    return {"x" : marksInPercentage, "y": daysPresent}

def findCorrelation(datasource):
    correlation = n.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days present :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data/data.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()
