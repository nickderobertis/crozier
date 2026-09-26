

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ImageMessageType(enum.StrEnum):
    """
    The type of message to send. You must provide `image` in this field
    """

    IMAGE = "image"

    def visit(self, image: typing.Callable[[], T_Result]) -> T_Result:
        if self is ImageMessageType.IMAGE:
            return image()
