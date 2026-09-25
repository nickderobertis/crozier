

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemValueType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    REALM_USER_SETTINGS_DEFAULTS = "realm_user_settings_defaults"

    def visit(self, realm_user_settings_defaults: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemValueType.REALM_USER_SETTINGS_DEFAULTS:
            return realm_user_settings_defaults()
