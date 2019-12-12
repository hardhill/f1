from flask import Flask, jsonify,abort,make_response
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


@app.route('/')
def hello_world():
    return "Hello World"



@app.route("/user")
def user_name():
    return jsonify({'tasks': tasks})

@app.route("/user/<int:id>", methods=["GET"])
def user_name_id(id):
    user = list(filter(lambda t: t["id"]==id,tasks))
    if len(user)==0:
        abort(404)
    return jsonify({"user":user})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(debug=True)
