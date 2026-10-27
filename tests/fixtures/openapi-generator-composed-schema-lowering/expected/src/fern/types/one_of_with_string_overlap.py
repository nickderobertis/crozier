

import typing

from .open_string_model import OpenStringModel
from .string_enum_model import StringEnumModel

OneOfWithStringOverlap = typing.Union[OpenStringModel, StringEnumModel]
