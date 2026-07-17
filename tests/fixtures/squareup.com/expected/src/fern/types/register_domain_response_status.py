

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RegisterDomainResponseStatus(enum.StrEnum):
    """
    The status of the domain registration.
    """

    PENDING = "PENDING"
    VERIFIED = "VERIFIED"

    def visit(self, pending: typing.Callable[[], T_Result], verified: typing.Callable[[], T_Result]) -> T_Result:
        if self is RegisterDomainResponseStatus.PENDING:
            return pending()
        if self is RegisterDomainResponseStatus.VERIFIED:
            return verified()
