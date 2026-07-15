

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConnectionStatus(str, enum.Enum):
    """
    Status of the connection.
    """

    LIVE = "live"
    UPCOMING = "upcoming"
    REQUESTED = "requested"

    def visit(
        self,
        live: typing.Callable[[], T_Result],
        upcoming: typing.Callable[[], T_Result],
        requested: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConnectionStatus.LIVE:
            return live()
        if self is ConnectionStatus.UPCOMING:
            return upcoming()
        if self is ConnectionStatus.REQUESTED:
            return requested()
