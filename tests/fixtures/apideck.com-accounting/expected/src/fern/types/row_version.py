

import typing

RowVersion = typing.Optional[str]
"""
A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.
"""
