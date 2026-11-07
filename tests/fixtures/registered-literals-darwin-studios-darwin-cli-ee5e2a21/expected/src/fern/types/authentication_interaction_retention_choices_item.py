

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationInteractionRetentionChoicesItem(enum.StrEnum):
    TEMPORARY = "temporary"
    SAVED = "saved"

    def visit(self, temporary: typing.Callable[[], T_Result], saved: typing.Callable[[], T_Result]) -> T_Result:
        if self is AuthenticationInteractionRetentionChoicesItem.TEMPORARY:
            return temporary()
        if self is AuthenticationInteractionRetentionChoicesItem.SAVED:
            return saved()
