from flask import Flask,jsonify,render_template,request
import config
from utils import Term_deposit

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/Term_deposit",methods=['POST','GET'])
def get_td():
    if request.method == "POST":
        data = request.form
        
        print("we are using POST")

        age                    = eval(data["age"])
        job                    = data["job"]
        marital                = data["marital"]
        education              = data["education"] 
        default                = data["default"]
        balance                = eval(data["balance"])
        housing                = data["housing"]
        loan                   = data["loan"]
        contact                = data["contact"]
        day                    = eval(data["day"])
        month                  = data["month"]
        duration               = eval(data["duration"])
        campaign               = eval(data["campaign"]) 
        pdays                  = eval(data["pdays"])
        previous               = eval(data["previous"]) 
    

    td_obj = Term_deposit(age,job,marital,education,default,balance,housing,loan,contact,day,month,duration,campaign,pdays,previous)
    td = td_obj.get_prediction()
    return jsonify({"will client subscribe to term-deposit ?":td})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUM_1)