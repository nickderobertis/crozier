

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConnectorEventEventSource(enum.StrEnum):
    """
    Unify event source
    """

    NATIVE = "native"
    VIRTUAL = "virtual"

    def visit(self, native: typing.Callable[[], T_Result], virtual: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConnectorEventEventSource.NATIVE:
            return native()
        if self is ConnectorEventEventSource.VIRTUAL:
            return virtual()
