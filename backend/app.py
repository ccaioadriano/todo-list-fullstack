from flask import Flask, jsonify

app = Flask(__name__)

api = "tarefas"


@app.route("/tarefas")
def getAllTasks():

    # Fazer um Select no BD
    
    tasks = [
        {
            "id": 1,
            "title": "Title",
            "description": "Description",
            "completed": True,
        }
    ]

    return jsonify(tasks)


@app.route("/tarefas/<int:id_task>")
def getTaskById(id_task):

    #Fazer um metodo que busca uma task via id no BD
    return jsonify({
        "id": id_task,
        "title": "Task via parametro",
        "description": "Task Passada via URL",
        "completed": False,
    })


if __name__ == '__main__':
    app.run(debug=True)
