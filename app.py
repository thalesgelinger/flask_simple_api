from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route("/users")
def get_users():
    page = int(request.args.get("page"))
    pageSize = int(request.args.get("pageSize"))
    end = page*pageSize
    start = end-pageSize
    return jsonify(users[start:end])

@app.route("/users", methods=['POST'])
def add_user():
    user = request.json
    user["id"] = len(users)
    users.append(user)
    return jsonify(user)

@app.route("/users/<int:id>", methods=['DELETE'])
def delete_user(id):
    deleted_user = users.pop(id)
    return jsonify(deleted_user)

if __name__ == "__main__":
    app.run(use_reloader=True)