

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AdsAdapterStatusRegion(enum.StrEnum):
    NA = "na"
    EU = "eu"
    FE = "fe"

    def visit(
        self, na: typing.Callable[[], T_Result], eu: typing.Callable[[], T_Result], fe: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is AdsAdapterStatusRegion.NA:
            return na()
        if self is AdsAdapterStatusRegion.EU:
            return eu()
        if self is AdsAdapterStatusRegion.FE:
            return fe()
