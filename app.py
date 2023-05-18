from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template("paginas/index.html", \
        titulo_pagina="Página inicial")
    
@app.route("/times")
def categorias():
    return render_template("paginas/times.html", \
        titulo_pagina="Times")

@app.route("/jogadores")
def produto():
    return render_template("paginas/jogadores.html", \
        titulo_pagina="Jogadores")
    
@app.route("/resultado")
def carrinho():
    return render_template("paginas/resultado.html", \
        titulo_pagina="Resultados")

@app.route("/realmadrid")
def realmadrid():
    return render_template("paginas/realmadrid.html", \
        titulo_pagina="Real Madrid Jogadores")

@app.route("/realmadridres")
def realmadridres():
    return render_template("paginas/realmadridres.html", \
        titulo_pagina="Real Madrid Resultados")

@app.route("/manunited")
def manunited():
    return render_template("paginas/manunited.html", \
        titulo_pagina="Man United Jogadores")

@app.route("/manunitedres")
def manunitedres():
    return render_template("paginas/manunitedres.html", \
        titulo_pagina="Man United Resultados")

@app.route("/psg")
def psg():
    return render_template("paginas/psg.html", \
        titulo_pagina="PSG Jogadores")

@app.route("/psgres")
def psgres():
    return render_template("paginas/psgres.html", \
        titulo_pagina="PSG Resultados")

@app.route("/juventus")
def juventus():
    return render_template("paginas/juventus.html", \
        titulo_pagina="Juventus Jogadores")

@app.route("/juventusres")
def juventusres():
    return render_template("paginas/juventusres.html", \
        titulo_pagina="Juventus Resultados")

@app.route("/bayern")
def bayern():
    return render_template("paginas/bayern.html", \
        titulo_pagina="Bayern Jogadores")

@app.route("/bayernres")
def bayernres():
    return render_template("paginas/bayernres.html", \
        titulo_pagina="Bayern Resultados")

if __name__ == "__main__":
    app.run(debug=True)
