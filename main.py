from flask import Flask, render_template, json, jsonify
from bios import DmiParser, bios
from cache import DmiParser, cache
from physical_memory import DmiParser, phy
from baseboard import DmiParser, baseboard
from memory import DmiParser, text
app = Flask(__name__)


@app.route("/")
def hello():

    return render_template("hello.html")


@app.route("/memory")
def mem():
    parser = DmiParser(text)
    dmidata = json.loads(str(parser))
    return json.dumps(dmidata)


@app.route("/bios")
def bio():
    parser = DmiParser(bios)
    dmidata = json.loads(str(parser))
    return json.dumps(dmidata)


@app.route("/baseboard")
def bas():
    parser = DmiParser(baseboard)
    dmidata = json.loads(str(parser))
    return json.dumps(dmidata)


@app.route("/physical_memory")
def ph():
    parser = DmiParser(phy)
    dmidata = json.loads(str(parser))
    return json.dumps(dmidata)


@app.route("/cache")
def cach():
    parser = DmiParser(cache)
    dmidata = json.loads(str(parser))
    return json.dumps(dmidata)


if '__name__'=='__main__':
    app.run(debug=True)