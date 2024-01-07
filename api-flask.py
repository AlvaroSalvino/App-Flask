from flask import Flask, jsonify

app = Flask(__name__)

itens = [
    {
        "nome": "Teclado",
        "Preco": 25.90
    },
    {
        "nome": "Mouse",
        "Preco": 20.88
    },
    {
        "nome": "Cadeira Gamer",
        "Preco": 2000.00
    }
]

@app.route("/")
def motraItens():
    return jsonify(itens)
@app.route("/itens/<int:id>")
def mostrarIntesPorId(id):
    return(jsonify(itens[id]))

if __name__=="__main__":
    app.run(debug= True)