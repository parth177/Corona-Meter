import os
import requests
from flask import Flask,render_template,request

app=Flask(__name__)


@app.route("/")
def corona():
    res=requests.get("https://api.covid19india.org/data.json")
    if res.status_code != 200:
        raise Exception("ERROR:API request unsuccessful.")
    data = res.json()
    return render_template("corona.html",data=data["statewise"])

@app.route("/corona/state_wise/<string:state>")
def statewise(state):
    try:    
        res=requests.get("https://api.covid19india.org/state_district_wise.json")
        if res.status_code != 200:
            raise Exception("ERROR:API request unsuccessful.")
        data = res.json()
        state_data=data[state]
    except KeyError:
        return "<h1 style='background-color: #e3f2fd'>Information for this state not available<h1>"
    
    return render_template("statewise.html",state_data=state_data,state=state)
app.run(debug=True)