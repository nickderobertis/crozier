

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class ListCustomCodeBlocksScriptsResponseBlocksItemType(enum.StrEnum):
    """
    Whether the Custom Code script is applied at the Site-level or Page-level
    """

    PAGE = "page"
    SITE = "site"

    def visit(self, page: typing.Callable[[], T_Result], site: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListCustomCodeBlocksScriptsResponseBlocksItemType.PAGE:
            return page()
        if self is ListCustomCodeBlocksScriptsResponseBlocksItemType.SITE:
            return site()
