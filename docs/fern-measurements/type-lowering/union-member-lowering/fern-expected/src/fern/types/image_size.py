

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ImageSize(enum.StrEnum):
    """
    Image positioning and size
    """

    LARGE = "Large"
    PREVIEW = "Preview"

    def visit(self, large: typing.Callable[[], T_Result], preview: typing.Callable[[], T_Result]) -> T_Result:
        if self is ImageSize.LARGE:
            return large()
        if self is ImageSize.PREVIEW:
            return preview()
