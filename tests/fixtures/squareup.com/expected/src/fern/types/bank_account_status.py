

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BankAccountStatus(str, enum.Enum):
    """
    Indicates the current verification status of a `BankAccount` object.
    """

    VERIFICATION_IN_PROGRESS = "VERIFICATION_IN_PROGRESS"
    VERIFIED = "VERIFIED"
    DISABLED = "DISABLED"

    def visit(
        self,
        verification_in_progress: typing.Callable[[], T_Result],
        verified: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BankAccountStatus.VERIFICATION_IN_PROGRESS:
            return verification_in_progress()
        if self is BankAccountStatus.VERIFIED:
            return verified()
        if self is BankAccountStatus.DISABLED:
            return disabled()
