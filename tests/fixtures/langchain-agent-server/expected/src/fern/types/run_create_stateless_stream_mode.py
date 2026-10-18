

import typing

from .run_create_stateless_stream_mode_one import RunCreateStatelessStreamModeOne
from .run_create_stateless_stream_mode_zero_item import RunCreateStatelessStreamModeZeroItem

RunCreateStatelessStreamMode = typing.Union[
    typing.List[RunCreateStatelessStreamModeZeroItem], RunCreateStatelessStreamModeOne
]
