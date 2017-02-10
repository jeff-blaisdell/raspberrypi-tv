import devices
from flask import Flask, jsonify, request
from not_found import NotFound
from execute_command_failure import ExecuteCommandFailure

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


@app.route("/execute", methods=['POST'])
def execute():
    req_json = request.get_json()
    devices.execute(req_json['text'])
    return "", 204


@app.route("/devices", methods=['GET'])
def list_devices():
    commands = devices.list_devices()
    return jsonify(commands)


@app.route("/devices/<string:device_id>/commands", methods=['GET'])
def list_device_commands(device_id):
    commands = devices.list_device_commands(device_id.lower())
    return jsonify(commands)


@app.route("/devices/<string:device_id>/commands/<string:command_id>", methods=['GET'])
def get_device_command(device_id, command_id):
    command = devices.get_device_command(device_id.lower(), command_id.lower())
    return jsonify(command)


@app.route("/devices/<string:device_id>/commands/<string:command_id>", methods=['POST'])
def execute_device_command(device_id, command_id):
    devices.execute_device_command(device_id.lower(), command_id.lower())
    return "", 204


@app.errorhandler(NotFound)
def handle_not_found(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(ExecuteCommandFailure)
def handle_execute_command_failure(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')
