

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EreaderDeviceObjectAvailabilityOption(enum.StrEnum):
    """
    The availability option for the device.
    """

    ADMIN_OR_UP = "adminOrUp"
    USER_OR_UP = "userOrUp"
    GUEST_OR_UP = "guestOrUp"
    SPECIFIC_USERS = "specificUsers"

    def visit(
        self,
        admin_or_up: typing.Callable[[], T_Result],
        user_or_up: typing.Callable[[], T_Result],
        guest_or_up: typing.Callable[[], T_Result],
        specific_users: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EreaderDeviceObjectAvailabilityOption.ADMIN_OR_UP:
            return admin_or_up()
        if self is EreaderDeviceObjectAvailabilityOption.USER_OR_UP:
            return user_or_up()
        if self is EreaderDeviceObjectAvailabilityOption.GUEST_OR_UP:
            return guest_or_up()
        if self is EreaderDeviceObjectAvailabilityOption.SPECIFIC_USERS:
            return specific_users()
