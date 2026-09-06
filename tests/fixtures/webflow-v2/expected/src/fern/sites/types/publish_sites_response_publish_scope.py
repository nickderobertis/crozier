

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PublishSitesResponsePublishScope(enum.StrEnum):
    """
    Whether the site or an individual page was published
    """

    SITE = "site"
    PAGE = "page"

    def visit(self, site: typing.Callable[[], T_Result], page: typing.Callable[[], T_Result]) -> T_Result:
        if self is PublishSitesResponsePublishScope.SITE:
            return site()
        if self is PublishSitesResponsePublishScope.PAGE:
            return page()
