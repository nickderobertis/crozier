

import typing

ManagerType = typing.Union[
    typing.Literal["round_robin", "supervisor", "dynamic", "sleeptime", "voice_sleeptime", "swarm"], typing.Any
]
