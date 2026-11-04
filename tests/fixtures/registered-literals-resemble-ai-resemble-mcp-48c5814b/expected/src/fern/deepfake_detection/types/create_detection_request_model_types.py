

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateDetectionRequestModelTypes(enum.StrEnum):
    """
    Use talking_head for face-swaps
    """

    IMAGE = "image"
    TALKING_HEAD = "talking_head"

    def visit(self, image: typing.Callable[[], T_Result], talking_head: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateDetectionRequestModelTypes.IMAGE:
            return image()
        if self is CreateDetectionRequestModelTypes.TALKING_HEAD:
            return talking_head()
