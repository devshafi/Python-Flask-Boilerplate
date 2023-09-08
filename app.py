from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample initial todo list
todos = [{'id': 1, 'task': 'Learn Flask', 'done': False}]


# main route
@app.route('/')
def index():
    return render_template('index.html', todos=todos)


# route for add/get todo(s)
@app.route('/api/todos', methods=['GET', 'POST'])
def api_todos():
    if request.method == 'GET':
        return jsonify(todos)
    elif request.method == 'POST':
        data = request.get_json()
        if 'task' in data:
            new_todo = {
                'id': len(todos) + 1,
                'task': data['task'],
                'done': False
            }
            todos.append(new_todo)
            return jsonify(new_todo), 201
        else:
            return jsonify({'error': 'Task is required'}), 400

if __name__ == '__main__':
    app.run(debug=True)
