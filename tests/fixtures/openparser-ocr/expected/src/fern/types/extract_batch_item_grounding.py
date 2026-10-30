

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtractBatchItemGrounding(enum.StrEnum):
    """
    Optional field grounding mode. Defaults to `none`. `field` opts into verified
    per-leaf citations and is part of idempotency identity.
    """

    NONE = "none"
    FIELD = "field"

    def visit(self, none: typing.Callable[[], T_Result], field: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExtractBatchItemGrounding.NONE:
            return none()
        if self is ExtractBatchItemGrounding.FIELD:
            return field()
