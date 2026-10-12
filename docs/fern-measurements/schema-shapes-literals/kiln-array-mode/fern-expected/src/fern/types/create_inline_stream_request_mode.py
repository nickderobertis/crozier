

import typing

from .create_inline_stream_request_mode_one import CreateInlineStreamRequestModeOne
from .create_inline_stream_request_mode_zero_item import CreateInlineStreamRequestModeZeroItem

CreateInlineStreamRequestMode = typing.Union[
    typing.List[CreateInlineStreamRequestModeZeroItem], CreateInlineStreamRequestModeOne
]
