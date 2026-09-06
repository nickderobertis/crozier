

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SystemEnum(enum.StrEnum):
    """
    The system to which the domain user belongs to
    """

    DIRECTORY = "Directory"
    SERVICE_DESK = "Service Desk"
    DISPUTE_RESOLUTION = "Dispute Resolution"
    PORTAL = "Portal"
    CENTRALIZED_PLATFORM = "Centralized Platform"

    def visit(
        self,
        directory: typing.Callable[[], T_Result],
        service_desk: typing.Callable[[], T_Result],
        dispute_resolution: typing.Callable[[], T_Result],
        portal: typing.Callable[[], T_Result],
        centralized_platform: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SystemEnum.DIRECTORY:
            return directory()
        if self is SystemEnum.SERVICE_DESK:
            return service_desk()
        if self is SystemEnum.DISPUTE_RESOLUTION:
            return dispute_resolution()
        if self is SystemEnum.PORTAL:
            return portal()
        if self is SystemEnum.CENTRALIZED_PLATFORM:
            return centralized_platform()
