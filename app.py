from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/jugadores")
def jugadores():
    return render_template("jugadores.html")

@app.route("/calendario")
def calendario():
    return render_template("calendario.html")

@app.route("/inscripcion")
def inscripcion():
    return render_template("registro.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)