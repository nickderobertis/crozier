

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtractRequestGrounding(enum.StrEnum):
    """
    Optional field grounding mode. Defaults to `none` for inline requests. Changing
    grounding with the same Idempotency-Key returns `409 idempotency_conflict`.
    Unsupported schemas return `422 grounding_unsupported_schema`.
    """

    NONE = "none"
    FIELD = "field"

    def visit(self, none: typing.Callable[[], T_Result], field: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExtractRequestGrounding.NONE:
            return none()
        if self is ExtractRequestGrounding.FIELD:
            return field()
