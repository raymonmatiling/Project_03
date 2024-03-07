import psycopg2
from flask import Flask, jsonify

connection = psycopg2.connect(database="Climate_Change_Analysis", user="postgres", password="postgres", host="localhost", port=5432)
cursor = connection.cursor()

cursor.execute("SELECT * from annual_emissions;")
annualEmissions = cursor.fetchall()

cursor.execute("SELECT * from per_capita_emissions;")
perCapitaEmissions = cursor.fetchall()

# print("annual Data from Database:- ", annualEmissions)
# print("per capita Data from Database:- ", perCapitaEmissions)

app = Flask(__name__)

@app.route("/api/v1.0/annualEmissions")
def annualEmissionsData():
    annualEmissionList = []
    for country, code, year, emission in annualEmissions:
        for x in range(1960, 2023):
            if(x == year):
                emissionDict = {}
                emissionDict["country"] = country
                emissionDict["year"] = year
                emissionDict["emission"] = emission
                emissionDict["code"] = code
                annualEmissionList.append(emissionDict)
    # print(currentEmissionList)
    response = jsonify(annualEmissionList)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/api/v1.0/emissionsPerPerson")
def emissionsPerPerson():
    ppEmissionsList = []
    for country, code, year, emission in perCapitaEmissions:
        for x in range(1960, 2023):
            if(x == year):
                emissionDict = {}
                emissionDict["country"] = country
                emissionDict["year"] = year
                emissionDict["emission"] = emission
                emissionDict["code"] = code
                ppEmissionsList.append(emissionDict)
    # print(currentEmissionList)
    response = jsonify(ppEmissionsList)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)