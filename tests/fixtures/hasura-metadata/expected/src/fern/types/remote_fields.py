

import typing

from .field_call import FieldCall

RemoteFields = typing.Dict[str, FieldCall]
"""
Remote fields are represented by an object that maps each field name to its arguments.
"""
