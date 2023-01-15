# -*- coding: utf-8 -*-

import json,formulas
import data as data
from flask import Flask,request,jsonify
from flask_cors import CORS
import sys
import csv
from data import read_csv_file, return_result
from formulas import calculate
import scraper

app=Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def results():
    try:
        payload = request.get_json()
        university = payload['university']
        field_of_study = payload['fieldOfStudy']
        results = payload['results']
    

        subjects = ["Fizyka", "Biologia", "Chemia", "Informatyka", "Matematyka", "Geografia", "Historia", "Filozofia"]

        M = 0
        G1 = 0
        G2 = 0
        
        if university == "AGH":
            if field_of_study not in ["Ceramika", "Informatyka Społeczna", "Socjologia", "Kulturoznawstwo"]:
                for result in results:
                    if result['subject'] in subjects:
                        if result['subject'] == "Matematyka" and result['level'] == "Podstawowy":
                                M = result['score']
                        if result['score'] * 3 > G1:
                            G1 = result['score'] * 3
                        elif result['score'] > G2:
                            G2 = result['score']

                return jsonify({'result': (G1 * 3 + G2 + M) * 2})
            else:
                for result in results:
                    if result['subject'] in subjects:
                        if result['subject'] == "Matematyka" and result['level'] == "Podstawowy":
                            M = int(result['score'])
                        elif int(result['score']) > G1:
                            G1 = int(result['score'])
                        elif int(result['score']) > G2:
                            G2 = int(result['score'])

                return jsonify({'result': (G1 * 3 + G2 + M) * 2})
        else:
            return jsonify()
    except: 
        return jsonify()

if __name__=='__main__':
    app.run(port=5000)
