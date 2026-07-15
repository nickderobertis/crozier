

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConnectorEventEventSource(str, enum.Enum):
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
