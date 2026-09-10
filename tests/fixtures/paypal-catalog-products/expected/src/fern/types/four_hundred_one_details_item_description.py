

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FourHundredOneDetailsItemDescription(enum.StrEnum):
    ACCOUNT_VALIDATIONS_FAILED_FOR_THE_USER = "Account validations failed for the user."

    def visit(self, account_validations_failed_for_the_user: typing.Callable[[], T_Result]) -> T_Result:
        if self is FourHundredOneDetailsItemDescription.ACCOUNT_VALIDATIONS_FAILED_FOR_THE_USER:
            return account_validations_failed_for_the_user()
