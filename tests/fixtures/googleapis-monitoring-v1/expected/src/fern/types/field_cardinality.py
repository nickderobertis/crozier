

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FieldCardinality(enum.StrEnum):
    """
    The field cardinality.
    """

    CARDINALITY_UNKNOWN = "CARDINALITY_UNKNOWN"
    CARDINALITY_OPTIONAL = "CARDINALITY_OPTIONAL"
    CARDINALITY_REQUIRED = "CARDINALITY_REQUIRED"
    CARDINALITY_REPEATED = "CARDINALITY_REPEATED"

    def visit(
        self,
        cardinality_unknown: typing.Callable[[], T_Result],
        cardinality_optional: typing.Callable[[], T_Result],
        cardinality_required: typing.Callable[[], T_Result],
        cardinality_repeated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FieldCardinality.CARDINALITY_UNKNOWN:
            return cardinality_unknown()
        if self is FieldCardinality.CARDINALITY_OPTIONAL:
            return cardinality_optional()
        if self is FieldCardinality.CARDINALITY_REQUIRED:
            return cardinality_required()
        if self is FieldCardinality.CARDINALITY_REPEATED:
            return cardinality_repeated()
