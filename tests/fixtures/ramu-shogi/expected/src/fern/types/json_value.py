

from __future__ import annotations

import typing

JsonValue = typing.Union[
    str, float, bool, typing.List[typing.Optional["JsonValue"]], typing.Dict[str, typing.Optional["JsonValue"]]
]
