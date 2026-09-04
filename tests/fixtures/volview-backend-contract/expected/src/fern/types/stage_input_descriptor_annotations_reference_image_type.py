

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StageInputDescriptorAnnotationsReferenceImageType(enum.StrEnum):
    IMAGE = "image"

    def visit(self, image: typing.Callable[[], T_Result]) -> T_Result:
        if self is StageInputDescriptorAnnotationsReferenceImageType.IMAGE:
            return image()
