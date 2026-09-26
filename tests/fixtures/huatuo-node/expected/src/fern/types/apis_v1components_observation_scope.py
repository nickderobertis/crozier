

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApisV1ComponentsObservationScope(enum.StrEnum):
    """
    Boundary observed by an on-demand operation.
    """

    HOST = "host"
    CONTAINER = "container"

    def visit(self, host: typing.Callable[[], T_Result], container: typing.Callable[[], T_Result]) -> T_Result:
        if self is ApisV1ComponentsObservationScope.HOST:
            return host()
        if self is ApisV1ComponentsObservationScope.CONTAINER:
            return container()
