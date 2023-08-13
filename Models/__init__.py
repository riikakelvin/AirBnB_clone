'''
models/__init__.py

This module is likethe entry point for the models package.

It initializes the FileStorage instance and reloads data from
the JSON file.

Usage:
    - Import modules or packages from the models package to access
    the defined classes.

    - Use the `storage` variable to interact with the FileStorage instance.

Example:
    from models import storage
    '''

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
