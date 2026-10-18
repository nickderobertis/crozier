

import typing

from .send import Send

CommandGoto = typing.Union[Send, typing.List[Send], str, typing.List[str]]
