

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchImagesRequestAspectRatio(enum.StrEnum):
    TALL = "tall"
    WIDE = "wide"
    SQUARE = "square"

    def visit(
        self,
        tall: typing.Callable[[], T_Result],
        wide: typing.Callable[[], T_Result],
        square: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchImagesRequestAspectRatio.TALL:
            return tall()
        if self is SearchImagesRequestAspectRatio.WIDE:
            return wide()
        if self is SearchImagesRequestAspectRatio.SQUARE:
            return square()
