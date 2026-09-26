

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdatePresenceRequestStatus(enum.StrEnum):
    """
    The status of the user on this client.

    Clients should report the user as `"active"` on this device if the client
    knows that the user is presently using the device (and thus would
    potentially see a notification immediately), even if the user
    has not directly interacted with the Zulip client.

    Otherwise, it should report the user as `"idle"`.

    See the related [`new_user_input`](#parameter-new_user_input) parameter
    for how a client should report whether the user is actively using the
    Zulip client.
    """

    IDLE = "idle"
    ACTIVE = "active"

    def visit(self, idle: typing.Callable[[], T_Result], active: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdatePresenceRequestStatus.IDLE:
            return idle()
        if self is UpdatePresenceRequestStatus.ACTIVE:
            return active()
