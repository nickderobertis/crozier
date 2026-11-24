

from __future__ import annotations

import typing

JsonValue = typing.Union[
    str, int, float, bool, typing.Dict[str, typing.Optional["JsonValue"]], typing.List[typing.Optional["JsonValue"]]
]
