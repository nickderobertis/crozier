

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContainerSpecServiceType(enum.StrEnum):
    """
    Service type identifier (must be "container")
    """

    CONTAINER = "container"

    def visit(self, container: typing.Callable[[], T_Result]) -> T_Result:
        if self is ContainerSpecServiceType.CONTAINER:
            return container()
