

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListTagsRequestOrderBy(enum.StrEnum):
    """
    Field to sort by
    """

    NAME = "name"

    def visit(self, name: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListTagsRequestOrderBy.NAME:
            return name()
