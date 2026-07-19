

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchArchivalMemoryRequestTagMatchMode(enum.StrEnum):
    """
    How to match tags - 'any' to match passages with any of the tags, 'all' to match only passages with all tags
    """

    ANY = "any"
    ALL = "all"

    def visit(self, any: typing.Callable[[], T_Result], all_: typing.Callable[[], T_Result]) -> T_Result:
        if self is SearchArchivalMemoryRequestTagMatchMode.ANY:
            return any()
        if self is SearchArchivalMemoryRequestTagMatchMode.ALL:
            return all_()
