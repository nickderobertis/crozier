

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateProductsRequestPublishStatus(enum.StrEnum):
    """
    Indicate whether your Product should be set as "staging" or "live"
    """

    STAGING = "staging"
    LIVE = "live"

    def visit(self, staging: typing.Callable[[], T_Result], live: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateProductsRequestPublishStatus.STAGING:
            return staging()
        if self is CreateProductsRequestPublishStatus.LIVE:
            return live()
