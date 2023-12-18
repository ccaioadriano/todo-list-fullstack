from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

api = "tarefas"

tasks = [
    {
        "id": 1,
        "title": "Title",
        "description": "Description",
        "completed": True,
    }
]


@app.route("/tarefas", methods=["GET"])
def getAllTasks():
    # Fazer um Select no BD
    if request.method == 'GET':
        return make_response(jsonify(tasks), 200)


@app.route("/tarefas", methods=["POST"])
def createTask():
    if request.method == 'POST':
        tasks.append(request.get_json())
        response = make_response(jsonify(tasks), 201)
        return response



@app.route("/tarefas/<int:id_task>")
def getTaskById(id_task):
    
    task = [item for item in tasks if item['id'] == id_task]
    response = make_response(jsonify(task), 200)
    return response


if __name__ == '__main__':
    app.run(debug=True)
