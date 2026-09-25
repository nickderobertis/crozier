

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemConsentedType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    REALM_EXPORT_CONSENT = "realm_export_consent"

    def visit(self, realm_export_consent: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemConsentedType.REALM_EXPORT_CONSENT:
            return realm_export_consent()
