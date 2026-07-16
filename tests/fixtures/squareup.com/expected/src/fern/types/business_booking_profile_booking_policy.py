

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BusinessBookingProfileBookingPolicy(enum.StrEnum):
    """
    Policies for accepting bookings.
    """

    ACCEPT_ALL = "ACCEPT_ALL"
    REQUIRES_ACCEPTANCE = "REQUIRES_ACCEPTANCE"

    def visit(
        self, accept_all: typing.Callable[[], T_Result], requires_acceptance: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is BusinessBookingProfileBookingPolicy.ACCEPT_ALL:
            return accept_all()
        if self is BusinessBookingProfileBookingPolicy.REQUIRES_ACCEPTANCE:
            return requires_acceptance()
