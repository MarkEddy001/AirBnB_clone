#!/usr/bin/python3
""" Create the initialiations needed for base_model

import file_storage.py
create the variable storage, an instance of FileStorage
call reload() method on this variable
"""

from .engine.file_storage import FileStorage
"""
Retrieves the storage instance
"""
storage = FileStorage()
storage.reload()
