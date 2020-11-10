from flask import Flask, json, render_template
import requests
app = Flask(__name__)


@app.route("/")
def get():

        return render_template("nav.html")


@app.route("/help")
def help():
        res = requests.get('http://127.0.0.1:5000/help')
        data = res.json()
        return render_template("help.html", abc=data)


@app.route("/processor")
def pro():
        pro = requests.get('http://127.0.0.1:5000/processor')
        data1 = pro.json()
        return render_template("processor.html", xyz=data1)


@app.route("/baseboard")
def bas():
        bas = requests.get('http://127.0.0.1:5000/baseboard')
        data2 = bas.json()
        return render_template("baseboard.html", pqr=data2)


@app.route("/memory")
def mem():
        mem = requests.get('http://127.0.0.1:5000/memory')
        data3 = mem.json()
        return render_template("memory.html", d=data3)


@app.route("/bios")
def bios():
        bios = requests.get('http://127.0.0.1:5000/bios')
        data5 = bios.json()
        return render_template("bios.html", bios=data5)


@app.route("/type")
def ty():
        ty = requests.get('http://127.0.0.1:5000/type')
        data4 = ty.json()
        return render_template("type.html", ty=data4)


if '__name__' == '__main__':
    app.route(debug=True, host="0.0.0.0", port=9109)

