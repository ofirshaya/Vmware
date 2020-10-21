import datetime
import requests
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash


def geturltime(url):
    try:
        r = requests.get(url, timeout=6)
        r.raise_for_status()
        status = str(r.status_code)
        print(status)
        if '200' in status:
            print ("work")
            status_code = '1'
        else:
            status_code = '0'
        respTime = str(round(r.elapsed.total_seconds(),2))
        responsemassage = "response time is :{} url is: {} response code is :{}".format(respTime , url , status_code )
        return responsemassage  
        print (respTime)
    except requests.exceptions.HTTPError as err01:
        print ("HTTP error: ", err01)
        status = str(r.status_code)
        if '200' in status:
            stauts_code = '1'
        else:
            stauts_code = '0'
        responsemassage = "{} the server is unreacheble response code is: {}".format(url,stauts_code)
        return responsemassage  
    except requests.exceptions.ConnectionError as err02:
        print ("Error connecting: ", err02)
    except requests.exceptions.Timeout as err03:
        print ("Timeout error:", err03)
    except requests.exceptions.RequestException as err04:
        print ("Error: ", err04)
    

def check_status(url):
    c = requests.get(url)
    if '200' in str(c):
        return 1
    else:
        return 0

app = Flask(__name__)
@app.route('/metrics')
def hello():
    url503 = "https://httpstat.us/503"
    url200 = "https://httpstat.us/200"
    resp503 = geturltime(url503)
    resp200 = geturltime(url200)
    return render_template("index.html" , resp503=resp503 , resp200=resp200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)


