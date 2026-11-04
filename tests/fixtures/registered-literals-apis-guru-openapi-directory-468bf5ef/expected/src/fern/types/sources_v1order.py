

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SourcesV1Order(enum.StrEnum):
    """
    An enumeration.
    """

    NAME = "name"

    def visit(self, name: typing.Callable[[], T_Result]) -> T_Result:
        if self is SourcesV1Order.NAME:
            return name()
