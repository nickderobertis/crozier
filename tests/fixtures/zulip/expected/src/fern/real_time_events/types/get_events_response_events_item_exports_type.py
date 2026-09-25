

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemExportsType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    REALM_EXPORT = "realm_export"

    def visit(self, realm_export: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemExportsType.REALM_EXPORT:
            return realm_export()
