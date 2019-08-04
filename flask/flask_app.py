from flask import Flask,redirect,render_template,request
from sense_hat import SenseHat

sense = SenseHat()

app = Flask(__name__) # imports required function or web

@app.route("/")
def start_app():
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    temprature = sense.get_temperature()
    humidity = round(humidity,2)
    pressure = round(pressure,2)
    humidity = round(humidity,2)
    data = {"temperature":temprature,"humidity":humidity,"pressure":pressure}
    return render_template("index.html",**data)


@app.route("/test",methods=["POST","GET"])
def get_message():
    if request.method == 'POST':
        message = request.form
        text= message['message']
        print(text)
        sense.show_message(text)
    return render_template("index.html")

if __name__== '__main__':
    app.run(host="0.0.0.0",port=80,debug="True")
