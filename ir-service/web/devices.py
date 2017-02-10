import os.path
import yaml
from time import sleep
import subprocess
from not_found import NotFound
from execute_command_failure import ExecuteCommandFailure
from os import listdir
from os.path import isfile, join

commands_dir = "/var/data/ir-service/commands"


def list_devices():
    return [f[:-4] for f in listdir(commands_dir) if isfile(join(commands_dir, f)) and f.endswith(".yml")]


def list_device_commands(device_id):
    device_yml = "{}/{}.yml".format(commands_dir, device_id)
    print("checking {} for device commands".format(device_yml))
    if not (os.path.isfile(device_yml)):
        raise NotFound("{} device not found".format(device_id))

    with open(device_yml, 'r') as f:
        return yaml.load(f.read())


def get_device_command(device_id, command_id):
    commands = list_device_commands(device_id)["commands"]
    if not (command_id in commands):
        raise NotFound("{} command not found for device {}".format(command_id, device_id))

    return commands[command_id]


def execute_device_command(device_id, command_id):
    command = get_device_command(device_id, command_id)
    if isinstance(command, list):
        for c in command:
            if isinstance(c, str) and (c.startswith("wait ")):
                millis = int(c[5:]) * 0.001
                sleep(millis)
            elif isinstance(c, dict):
                remote = c["remote"]
                key = c["key"]
                result = subprocess.call(["irsend", "SEND_ONCE", remote, key])
                if not result == 0:
                    raise ExecuteCommandFailure(
                        "Failed to execute action {} of command {} on device {}".format(c, command_id, device_id)
                    )


def execute(text):
    lowercase_text = text.lower()
    devices = [d for d in list_devices() if d in lowercase_text]
    device = next(iter(devices or []), None)
    if device:
        commands = [c for c in list_device_commands(device)["commands"] if c in lowercase_text]
        command = next(iter(commands or []), None)
        if command:
            execute_device_command(device, command)
            return
    raise NotFound("Device / Command not found for text {}".format(lowercase_text))

