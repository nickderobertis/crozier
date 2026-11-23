

from __future__ import annotations

import typing

from .json_value_zero import JsonValueZero

JsonValue = typing.Union[typing.Optional[JsonValueZero], typing.List["JsonValue"], typing.Dict[str, "JsonValue"]]
