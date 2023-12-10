#!/usr/bin/python3
"""
Create the initialiations needed for base_model
"""

from .engine.file_storage import FileStorage
"""
Retrieves the storage instance
"""
storage = FileStorage()
storage.reload()
