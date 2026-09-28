

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetLeadsV3RequestStatus(enum.StrEnum):
    NEW = "New"
    CONTACTED = "Contacted"
    TOUR_SCHEDULED = "Tour Scheduled"
    TOUR_COMPLETED = "Tour Completed"
    TOUR_NO_SHOW = "Tour No Show"
    DISCOVERY_DAY_SCHEDULED = "Discovery Day Scheduled"
    DISCOVERY_DAY_COMPLETED = "Discovery Day Completed"
    DISCOVERY_DAY_NO_SHOW = "Discovery Day No Show"
    WAITLISTED = "Waitlisted"
    ENROLLED = "Enrolled"
    LOST = "Lost"
    NO_STATUS = "No Status"

    def visit(
        self,
        new: typing.Callable[[], T_Result],
        contacted: typing.Callable[[], T_Result],
        tour_scheduled: typing.Callable[[], T_Result],
        tour_completed: typing.Callable[[], T_Result],
        tour_no_show: typing.Callable[[], T_Result],
        discovery_day_scheduled: typing.Callable[[], T_Result],
        discovery_day_completed: typing.Callable[[], T_Result],
        discovery_day_no_show: typing.Callable[[], T_Result],
        waitlisted: typing.Callable[[], T_Result],
        enrolled: typing.Callable[[], T_Result],
        lost: typing.Callable[[], T_Result],
        no_status: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetLeadsV3RequestStatus.NEW:
            return new()
        if self is GetLeadsV3RequestStatus.CONTACTED:
            return contacted()
        if self is GetLeadsV3RequestStatus.TOUR_SCHEDULED:
            return tour_scheduled()
        if self is GetLeadsV3RequestStatus.TOUR_COMPLETED:
            return tour_completed()
        if self is GetLeadsV3RequestStatus.TOUR_NO_SHOW:
            return tour_no_show()
        if self is GetLeadsV3RequestStatus.DISCOVERY_DAY_SCHEDULED:
            return discovery_day_scheduled()
        if self is GetLeadsV3RequestStatus.DISCOVERY_DAY_COMPLETED:
            return discovery_day_completed()
        if self is GetLeadsV3RequestStatus.DISCOVERY_DAY_NO_SHOW:
            return discovery_day_no_show()
        if self is GetLeadsV3RequestStatus.WAITLISTED:
            return waitlisted()
        if self is GetLeadsV3RequestStatus.ENROLLED:
            return enrolled()
        if self is GetLeadsV3RequestStatus.LOST:
            return lost()
        if self is GetLeadsV3RequestStatus.NO_STATUS:
            return no_status()
