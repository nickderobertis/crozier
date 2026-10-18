

import typing

from .run_create_stateful_stream_mode_one import RunCreateStatefulStreamModeOne
from .run_create_stateful_stream_mode_zero_item import RunCreateStatefulStreamModeZeroItem

RunCreateStatefulStreamMode = typing.Union[
    typing.List[RunCreateStatefulStreamModeZeroItem], RunCreateStatefulStreamModeOne
]
