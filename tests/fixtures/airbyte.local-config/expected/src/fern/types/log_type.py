

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class LogType(str, enum.Enum):
    """
    type/source of logs produced
    """

    SERVER = "server"
    SCHEDULER = "scheduler"

    def visit(self, server: typing.Callable[[], T_Result], scheduler: typing.Callable[[], T_Result]) -> T_Result:
        if self is LogType.SERVER:
            return server()
        if self is LogType.SCHEDULER:
            return scheduler()
