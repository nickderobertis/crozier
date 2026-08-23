

import datetime as dt
import typing

from .bbox import Bbox

InlineValue = typing.Union[
    typing.Optional[typing.Any],
    bool,
    dt.date,
    dt.datetime,
    str,
    int,
    float,
    typing.List[typing.Any],
    typing.Dict[str, typing.Any],
    Bbox,
]
