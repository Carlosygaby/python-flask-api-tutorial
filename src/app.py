from flask import Flask,jsonify,request

print(request.json)

app = Flask(__name__)

todos=[
   {"label":"My firts task", "done":False},
   {"label": "My second task","done":False}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text= jsonify(todos)
    return json_text

@app.route("/todos", method=["POST"])
def add_new_todo():
   request_body = request.json
   print("incoming request with the following body", request_body)
   return "Response for the POST todo"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)