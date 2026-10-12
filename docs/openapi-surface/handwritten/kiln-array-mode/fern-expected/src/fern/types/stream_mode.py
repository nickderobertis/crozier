

import typing

from .stream_mode_one import StreamModeOne
from .stream_mode_zero_item import StreamModeZeroItem

StreamMode = typing.Union[typing.List[StreamModeZeroItem], StreamModeOne]
