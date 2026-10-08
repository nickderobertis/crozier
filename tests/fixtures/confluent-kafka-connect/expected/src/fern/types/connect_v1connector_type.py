

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConnectV1ConnectorType(enum.StrEnum):
    """
    Type of connector, sink or source
    """

    SINK = "sink"
    SOURCE = "source"

    def visit(self, sink: typing.Callable[[], T_Result], source: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConnectV1ConnectorType.SINK:
            return sink()
        if self is ConnectV1ConnectorType.SOURCE:
            return source()
