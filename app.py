from flask import Flask, render_template, jsonify
import pandas as pd
from pythonping import ping

app = Flask(__name__)

def load_branches():
    df = pd.read_excel("data/branches.xlsx")
    return df.to_dict(orient="records")

def check_ping(ip):
    try:
        response = ping(ip, count=2, timeout=3)
        if response.success():
            return "UP"
        else:
            return "DOWN"
    except:
        return "DOWN"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/status")
def api_status():
    branches = load_branches()
    results = []

    for b in branches:
        status = check_ping(b["IP Address"])
        results.append({
            "branch": b["Branch"],
            "ip": b["IP Address"],
            "status": status
        })

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=Tree)
    #app.run(host="0.0.0.0", port=5000, debug=True)

