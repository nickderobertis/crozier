

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ImageBlockGroupType(enum.StrEnum):
    IMAGE = "IMAGE"

    def visit(self, image: typing.Callable[[], T_Result]) -> T_Result:
        if self is ImageBlockGroupType.IMAGE:
            return image()
