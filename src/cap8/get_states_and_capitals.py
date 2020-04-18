import json


def get_states_and_capitals():
    with open("./usa_state_capitals/states_and_capitals.json") as file:
        return json.load(file)