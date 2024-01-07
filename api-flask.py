from flask import Flask

app = Flask(__name__)

@app.route("/")
def motraItens():
    return "Itens do banco de dados"

if __name__=="__main__":
    app.run(debug= True)