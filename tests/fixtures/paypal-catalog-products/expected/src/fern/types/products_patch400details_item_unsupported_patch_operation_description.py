

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProductsPatch400DetailsItemUnsupportedPatchOperationDescription(enum.StrEnum):
    THE_SPECIFIED_PATCH_OPERATION_NOT_SUPPORTED_FOR_THIS_FIELD = (
        "The specified patch operation not supported for this field."
    )

    def visit(
        self, the_specified_patch_operation_not_supported_for_this_field: typing.Callable[[], T_Result]
    ) -> T_Result:
        if (
            self
            is ProductsPatch400DetailsItemUnsupportedPatchOperationDescription.THE_SPECIFIED_PATCH_OPERATION_NOT_SUPPORTED_FOR_THIS_FIELD
        ):
            return the_specified_patch_operation_not_supported_for_this_field()
