

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SitePublishPayloadPayloadPublishScope(enum.StrEnum):
    """
    Whether the entire site or an individual page was published
    """

    PAGE = "page"
    SITE = "site"

    def visit(self, page: typing.Callable[[], T_Result], site: typing.Callable[[], T_Result]) -> T_Result:
        if self is SitePublishPayloadPayloadPublishScope.PAGE:
            return page()
        if self is SitePublishPayloadPayloadPublishScope.SITE:
            return site()
