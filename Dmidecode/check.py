from flask import Flask, jsonify, render_template
from collections import defaultdict
import memory.py
import json
app = Flask(__name__)


@app.route("/cache")
def cache():
    f = open("SomeFile.txt",'r')

    data = f.readlines()

    while (data.count("\n")):
        data.remove("\n")

  #  dict1 = {}
    dict2 = {}

    for lines in data:
        if(lines.startswith("Handle")):
            h = lines[0:6]
            hv = lines[7:13]
            d = lines[15:23]
            dt = lines[24:-1]
            dict2[h] = hv
            dict2[d] = dt
        elif(lines.startswith("\tSocket")):
            s = lines[1:20]
            v = lines[21:-1]
            dict2[s] =v
        elif(lines.startswith("\tConfiguration:")):
            c = lines[1:14]
            v = lines[16:-1]
            dict2[c] = v
        elif(lines.startswith("\tOperational")):
            o = lines[1:17]
            v = lines[19:-1]
            dict2[o] = v
        elif(lines.startswith("\tLocation:")):
            l = lines[1:9]
            v = lines[11:-1]
            dict2[l] = v
        elif(lines.startswith("\tInstalled Size:")):
            i = lines[1:15]
            v = lines[17:-1]
            dict2[i] = v
        elif(lines.startswith("\tMaximum")):
            m = lines[1:13]
            v = lines[15:-1]
            dict2[m] = v
        elif(lines.startswith("\t\tSynchronous")):
            s = lines[2:-1]
            dict2['Supported SRAM Types']= s
        elif(lines.startswith("\tInstalled SRAM Type")):
            I = lines[1:20]
            v = lines[22:-1]
            dict2[I] = v
        elif(lines.startswith("\tSpeed:")):
            S = lines[1:6]
            v = lines[8:-1]
            dict2[S] = v
        elif(lines.startswith("\tError Correction Type:")):
            e = lines[1:22]
            v = lines[24:-1]
            dict2[e] = v
        elif(lines.startswith("\tSystem Type:")):
            s1 = lines[1:12]
            v = lines[14:-1]
            dict2[s1] = v
        elif(lines.startswith("\tAssociativity:")):
            a = lines[1:14]
            v = lines[16:-1]
            dict2[a] = v
           # dict1[dict2['Handle']] = dict2
            #print(len(dict1))
           # dict2={}
        else:
            pass

    #out_file = open("output.json","w")
    #obj = json.dump(dict1 , out_file , indent = (len(dict1)))
    #out_file.close()
    return json.dumps(dict2)
   # return render_template('cache.html', dict2=dict2)


@app.route("/bios")
def bios():
    f = open("bios.txt", 'r')
    data = f.readlines()

    while (data.count("\n")):
        data.remove("\n")

    dict2 = {}

    for lines in data:
        if (lines.startswith("Handle")):
            d = lines[0:6]
            a = lines[7:13]
            b = lines[15:23]
            c = lines[24:-1]
            dict2[d] = a
            dict2[b] = c
        elif (lines.startswith("\tVendor")):
            e = lines[9:-1]
            dict2['Vendor'] = e
        elif (lines.startswith("\tVersion")):
            f = lines[10:-1]
            dict2['Version'] = f
        elif (lines.startswith("\tRelease Date")):
            g = lines[14:-1]
            dict2['Release Date'] = g
        elif (lines.startswith("\tAddress")):
            h = lines[9:-1]
            dict2['Address'] = h
        elif (lines.startswith("\tRuntime Size")):
            i = lines[14:-1]
            dict2['Runtime Size'] = i
        elif (lines.startswith("\tROM Size")):
            j = lines[10:-1]
            dict2['ROM Size'] = j
        elif (lines.startswith("\tCharacteristics")):
            k = lines[17:-1]
            dict2['Characteristics'] = k
        elif (lines.startswith("\tLanguage Description Format")):
            o = lines[29:-1]
            dict2["Language Description Format"] = o
        elif (lines.startswith("\tInstallable Languages")):
            p = lines[23:-1]
            dict2["Installable Languages"] = p
        elif (lines.startswith("\tCurrently Installed Language")):
            q = lines[30:-1]
            dict2["Currently Installed Language"] = q

        else:
            pass

    #print(dict2)

    return json.dumps(dict2)


@app.route("/type")
def type():
    filename = 'type.txt'

    commands = {}
    with open(filename) as fh:
        for line in fh:
            command, description = line.strip().split(':', 1)
            commands[command] = description.strip()

    return json.dumps(commands)
   # return render_template('dict.html', commands=commands)


@app.route("/processor")
def processor():
    filename = 'processor.txt'

    commands = {}
    with open(filename) as fh:
        for line in fh:
            command, description = line.strip().split(':', 1)
            commands[command] = description.strip()
    return json.dumps(commands)
    #return render_template('dict.html', commands=commands)


@app.route("/memory")
def memory():
    d = defaultdict(list)

    with open("memory.txt") as fin:
        for line in fin:
            if ":" in line:
                k, v = line.rstrip().split(":")
                d[k].extend(map(str.strip, v.split(",")) if v.strip() else [])
            else:
                d[k].append(line.rstrip())
        return json.dumps(d)


@app.route("/baseboard")
def baseboard():
    filename = 'baseboard.txt'

    commands = {}
    with open(filename) as fh:
        for line in fh:
            command, description = line.strip().split(':', 1)
            commands[command] = description.strip()
    return json.dumps(commands)
   # return render_template('dict.html', commands=commands)


@app.route("/help", methods=['GET'])
def help():
    filename = 'help.txt'

    commands = {}
    with open(filename) as fh:
        for line in fh:
            command, description = line.strip().split(' ', 1)
            commands[command] = description.strip()

    return json.dumps(commands)
 #   return render_template('dict.html', commands=commands)
   # return json.dumps(commands), render_template('dict.html')


@app.route("/")
def base():

    return render_template('file2.html')


if "__name__" == "__main__":
    app.run(debug=True)

