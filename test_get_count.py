#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

first_state_id = list(storage.all(State).values())[0].id
<<<<<<< HEAD

print("First state: {}".format(storage.get(State, first_state_id)))
=======
print("First state: {}".format(storage.get(State, first_state_id)))

>>>>>>> 2d2acbbc0c3a651618d00602d0b6ef0003918c76
