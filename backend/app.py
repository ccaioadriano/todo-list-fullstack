from flask import Flask, jsonify

app = Flask(__name__)

api = "tarefas"


@app.route("/tarefas")
def home():

    tasks = [
        {
            "id": 1,
            "title": "Title",
            "description": "Description",
            "completed": True,
        }
    ]

    return jsonify(tasks)


if __name__ == '__main__':
    app.run(debug=True)
