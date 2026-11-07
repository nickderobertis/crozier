

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MenuItemSpecRouteRef(enum.StrEnum):
    """
    Built-in theme route resolved into status.href.
    """

    ARCHIVES = "archives"
    CATEGORIES = "categories"
    TAGS = "tags"

    def visit(
        self,
        archives: typing.Callable[[], T_Result],
        categories: typing.Callable[[], T_Result],
        tags: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MenuItemSpecRouteRef.ARCHIVES:
            return archives()
        if self is MenuItemSpecRouteRef.CATEGORIES:
            return categories()
        if self is MenuItemSpecRouteRef.TAGS:
            return tags()
