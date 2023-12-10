#!/usr/bin/python3
"""
Defines  the Amenity model
and inherits from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
 """ a class that defines a Amenity object that inherits from BaseModel

    Public class attributes:
    ------------------------

    name: string - empty string
    """
    name: str = ''
