#!/usr/bin/python3
"""
A module that contains the Review class that
defines all  attributes/methods for a Review object
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represent a review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
