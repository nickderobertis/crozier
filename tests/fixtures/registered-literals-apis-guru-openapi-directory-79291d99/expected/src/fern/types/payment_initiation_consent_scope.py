

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentInitiationConsentScope(enum.StrEnum):
    """
    Payment consent scope. Defines possible directions for payments made with the given consent.

    `ME_TO_ME`: Allows moving money between accounts owned by the same user.

    `EXTERNAL`: Allows initiating payments from the user's account to third parties.
    """

    ME_TO_ME = "ME_TO_ME"
    EXTERNAL = "EXTERNAL"

    def visit(self, me_to_me: typing.Callable[[], T_Result], external: typing.Callable[[], T_Result]) -> T_Result:
        if self is PaymentInitiationConsentScope.ME_TO_ME:
            return me_to_me()
        if self is PaymentInitiationConsentScope.EXTERNAL:
            return external()
