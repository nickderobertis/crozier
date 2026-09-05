

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchImagesRequestCategory(enum.StrEnum):
    PHOTOGRAPH = "photograph"
    ILLUSTRATION = "illustration"
    DIGITIZED_ARTWORK = "digitized_artwork"

    def visit(
        self,
        photograph: typing.Callable[[], T_Result],
        illustration: typing.Callable[[], T_Result],
        digitized_artwork: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchImagesRequestCategory.PHOTOGRAPH:
            return photograph()
        if self is SearchImagesRequestCategory.ILLUSTRATION:
            return illustration()
        if self is SearchImagesRequestCategory.DIGITIZED_ARTWORK:
            return digitized_artwork()
