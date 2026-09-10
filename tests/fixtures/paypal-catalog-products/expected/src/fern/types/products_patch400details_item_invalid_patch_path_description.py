

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProductsPatch400DetailsItemInvalidPatchPathDescription(enum.StrEnum):
    THE_SPECIFIED_FIELD_CANNOT_BE_PATCHED = "The specified field cannot be patched."

    def visit(self, the_specified_field_cannot_be_patched: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProductsPatch400DetailsItemInvalidPatchPathDescription.THE_SPECIFIED_FIELD_CANNOT_BE_PATCHED:
            return the_specified_field_cannot_be_patched()
