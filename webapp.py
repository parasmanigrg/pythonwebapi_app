#importing libraries
from flask import Flask, render_template, request, jsonify
import json
import requests



app = Flask(__name__)
summary_url_temp="https://api.covid19api.com/summary" #api link


@app.route('/', methods=['GET','POST'])
def home():
    
    response = requests.get(summary_url_temp)#get the response from the link
    if response.ok:
        resp_data=response.json() #convert the response into json format
        message=resp_data["Message"]
        if (message!=""):
            return(str(message) +"!! Please Refresh the page after few minutes")
        else:
            
            Global=resp_data["Global"]
            new_deaths= Global["NewDeaths"]
            total_deaths=Global["TotalDeaths"]
            new_cases= Global["NewConfirmed"]
            total_cases=Global["TotalConfirmed"]
            new_recovered= Global["NewRecovered"]
            total_recovered=Global["TotalRecovered"]
            updated=resp_data["Date"]

            return render_template("index.html",date=updated, nd_n=new_deaths, td_n=total_deaths,nc_n=new_cases,tc_n=total_cases,nr_n=new_recovered, tr_n=total_recovered)
    else:
        print(response.reason)




    
if __name__=="__main__":
    app.run(port=5085, debug="true")
