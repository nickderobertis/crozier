

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchImagesRequestSize(enum.StrEnum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

    def visit(
        self,
        small: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        large: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchImagesRequestSize.SMALL:
            return small()
        if self is SearchImagesRequestSize.MEDIUM:
            return medium()
        if self is SearchImagesRequestSize.LARGE:
            return large()
