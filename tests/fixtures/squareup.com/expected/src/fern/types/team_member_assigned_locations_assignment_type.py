

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TeamMemberAssignedLocationsAssignmentType(enum.StrEnum):
    """
    Enumerates the possible assignment types that the team member can have.
    """

    ALL_CURRENT_AND_FUTURE_LOCATIONS = "ALL_CURRENT_AND_FUTURE_LOCATIONS"
    EXPLICIT_LOCATIONS = "EXPLICIT_LOCATIONS"

    def visit(
        self,
        all_current_and_future_locations: typing.Callable[[], T_Result],
        explicit_locations: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TeamMemberAssignedLocationsAssignmentType.ALL_CURRENT_AND_FUTURE_LOCATIONS:
            return all_current_and_future_locations()
        if self is TeamMemberAssignedLocationsAssignmentType.EXPLICIT_LOCATIONS:
            return explicit_locations()
