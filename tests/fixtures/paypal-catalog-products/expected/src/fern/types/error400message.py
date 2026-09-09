

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Error400Message(enum.StrEnum):
    REQUEST_IS_NOT_WELL_FORMED_SYNTACTICALLY_INCORRECT_OR_VIOLATES_SCHEMA = (
        "Request is not well-formed, syntactically incorrect, or violates schema."
    )

    def visit(
        self, request_is_not_well_formed_syntactically_incorrect_or_violates_schema: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is Error400Message.REQUEST_IS_NOT_WELL_FORMED_SYNTACTICALLY_INCORRECT_OR_VIOLATES_SCHEMA:
            return request_is_not_well_formed_syntactically_incorrect_or_violates_schema()
