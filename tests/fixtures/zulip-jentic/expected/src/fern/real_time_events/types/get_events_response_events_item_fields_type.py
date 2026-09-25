

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemFieldsType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    CUSTOM_PROFILE_FIELDS = "custom_profile_fields"

    def visit(self, custom_profile_fields: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemFieldsType.CUSTOM_PROFILE_FIELDS:
            return custom_profile_fields()
