

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PageType(enum.StrEnum):
    """
    The node type. Identifies this node as a page in the structure tree.
    """

    PAGE = "page"

    def visit(self, page: typing.Callable[[], T_Result]) -> T_Result:
        if self is PageType.PAGE:
            return page()
