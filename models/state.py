#!/usr/bin/python3
"""
A module that contains the State class that
defines all  attributes/methods for a state object
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represent a state.

    Attributes:
        name (str): The name of the state.
    """
    name = ""
