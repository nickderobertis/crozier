

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AmazonSpapiProviderDetailsRegion(enum.StrEnum):
    NA = "na"
    EU = "eu"
    FE = "fe"

    def visit(
        self, na: typing.Callable[[], T_Result], eu: typing.Callable[[], T_Result], fe: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is AmazonSpapiProviderDetailsRegion.NA:
            return na()
        if self is AmazonSpapiProviderDetailsRegion.EU:
            return eu()
        if self is AmazonSpapiProviderDetailsRegion.FE:
            return fe()
