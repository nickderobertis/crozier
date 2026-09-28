

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WaitlistRequestSphere(enum.StrEnum):
    """
    Optional organization-sphere segment.
    """

    CAFE = "cafe"
    BEAUTY = "beauty"
    SERVICES = "services"
    RETAIL = "retail"
    OTHER = "other"

    def visit(
        self,
        cafe: typing.Callable[[], T_Result],
        beauty: typing.Callable[[], T_Result],
        services: typing.Callable[[], T_Result],
        retail: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WaitlistRequestSphere.CAFE:
            return cafe()
        if self is WaitlistRequestSphere.BEAUTY:
            return beauty()
        if self is WaitlistRequestSphere.SERVICES:
            return services()
        if self is WaitlistRequestSphere.RETAIL:
            return retail()
        if self is WaitlistRequestSphere.OTHER:
            return other()
