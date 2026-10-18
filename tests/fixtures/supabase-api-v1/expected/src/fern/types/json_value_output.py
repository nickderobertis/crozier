

from __future__ import annotations

import typing

from .json_value_output_zero import JsonValueOutputZero

JsonValueOutput = typing.Union[
    typing.Optional[JsonValueOutputZero], typing.List["JsonValueOutput"], typing.Dict[str, "JsonValueOutput"]
]
