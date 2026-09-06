

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateSkuProductsRequestPublishStatus(enum.StrEnum):
    """
    Indicate whether your Product should be set as "staging" or "live"
    """

    STAGING = "staging"
    LIVE = "live"

    def visit(self, staging: typing.Callable[[], T_Result], live: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateSkuProductsRequestPublishStatus.STAGING:
            return staging()
        if self is UpdateSkuProductsRequestPublishStatus.LIVE:
            return live()
