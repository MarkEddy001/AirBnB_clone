#!/usr/bin/python3
""" A module that contains the Review class that
defines all  attributes/methods for a Review object
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Definition of a Review."""
    place_id = ""
    user_id = ""
    text = ""
