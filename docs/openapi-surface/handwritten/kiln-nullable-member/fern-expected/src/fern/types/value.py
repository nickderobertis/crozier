

from __future__ import annotations

import typing

from .value_zero import ValueZero

Value = typing.Union[typing.Optional[ValueZero], typing.List["Value"]]
