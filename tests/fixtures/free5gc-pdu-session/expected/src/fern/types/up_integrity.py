

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpIntegrity(enum.StrEnum):
    REQUIRED = "REQUIRED"
    PREFERRED = "PREFERRED"
    NOT_NEEDED = "NOT_NEEDED"

    def visit(
        self,
        required: typing.Callable[[], T_Result],
        preferred: typing.Callable[[], T_Result],
        not_needed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpIntegrity.REQUIRED:
            return required()
        if self is UpIntegrity.PREFERRED:
            return preferred()
        if self is UpIntegrity.NOT_NEEDED:
            return not_needed()
