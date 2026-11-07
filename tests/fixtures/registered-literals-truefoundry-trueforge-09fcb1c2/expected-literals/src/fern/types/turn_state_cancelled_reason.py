

import typing

TurnStateCancelledReason = typing.Union[
    typing.Literal["server-execution-timeout", "client-cancelled", "cancelled-for-next-turn", "abandoned"], typing.Any
]
