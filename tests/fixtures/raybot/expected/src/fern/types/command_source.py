

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CommandSource(enum.StrEnum):
    """
    The source of the command
    """

    CLOUD = "CLOUD"

    def visit(self, cloud: typing.Callable[[], T_Result]) -> T_Result:
        if self is CommandSource.CLOUD:
            return cloud()
