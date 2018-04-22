from flask import Flask, jsonify, request
from Usuario import Usuario

app = Flask(__name__)

@app.route("/api", methods=['GET'])
def api():
    usuario = Usuario( "1", "Caio", "cvmartins1996@gmail.com")
    idUsuario = usuario.getId()
    nome = usuario.getNome()
    email = usuario.getEmail()
    hashEmail = usuario.getHashEmail()

    novo = Usuario("2", "Vinicius", "nome@hotmail.com")
    idUsuario2 = novo.getId()
    nome2 = novo.getNome()
    email2 = novo.getEmail()
    hashEmail2 = novo.getHashEmail()

    usuarios = jsonify({
        'usuario ' + idUsuario : {
            'id' : idUsuario,
            'nome' : nome,
            'email' : email,
            'email-crypto': str(hashEmail)
        },
        'usuario ' + idUsuario2 : {
            'id' : idUsuario2,
            'nome' : nome2,
            'email' : email2,
            'email-crypto': str(hashEmail2)
        }
    })
    
    return usuarios

@app.route("/")
def home():
    return "API"

if __name__ == '__main__':
    app.run(debug=True)

