

import typing

ReviewChangeAction = typing.Union[
    typing.Literal["SEND_FOR_REVIEW", "ACCEPT", "REJECT", "COMMENT", "RETRACT"], typing.Any
]
