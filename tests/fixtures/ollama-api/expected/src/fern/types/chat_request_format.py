

import typing

from .chat_request_format_zero import ChatRequestFormatZero

ChatRequestFormat = typing.Union[ChatRequestFormatZero, typing.Dict[str, typing.Any]]
