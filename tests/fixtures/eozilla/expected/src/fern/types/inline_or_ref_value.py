

import typing

from .inline_value import InlineValue
from .link import Link
from .qualified_value import QualifiedValue

InlineOrRefValue = typing.Union[Link, QualifiedValue, InlineValue]
