

import typing

StateMachineStateProcessResultDtoStateProcessType = typing.Union[
    typing.Literal["SUCCESS", "FAIL", "RESUBMIT", "UNKNOWN"], typing.Any
]
