

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class ReferenceFieldType(enum.StrEnum):
    """
    Choose these appropriate field type for your collection data
    """

    MULTI_REFERENCE = "MultiReference"
    REFERENCE = "Reference"

    def visit(
        self, multi_reference: typing.Callable[[], T_Result], reference: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is ReferenceFieldType.MULTI_REFERENCE:
            return multi_reference()
        if self is ReferenceFieldType.REFERENCE:
            return reference()
