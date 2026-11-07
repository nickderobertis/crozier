

import typing

from .advanced import Advanced
from .standard import Standard

ParameterCategory = typing.Union[Advanced, Standard]
