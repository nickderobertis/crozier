

from __future__ import annotations

import typing

QueryParameterValue = typing.Union[
    bool,
    int,
    float,
    str,
    typing.List[typing.Optional["QueryParameterValue"]],
    typing.Dict[str, typing.Optional["QueryParameterValue"]],
]
