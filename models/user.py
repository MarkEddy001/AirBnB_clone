#!/usr/bin/python3
""" A module that contains the User class that
defines all  attributes/methods for a user object
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class defining a User.

    Public class attributes:
    -----------------------
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
