from flask import Flask

app = Flask(__name__)

api = "tarefas"


@app.route("/tarefas")
def home():
    return {
        "message": "Ola Mundo"
    }


if __name__ == '__main__':
    app.run(debug=True)
