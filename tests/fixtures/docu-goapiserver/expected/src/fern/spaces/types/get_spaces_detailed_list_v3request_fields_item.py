

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSpacesDetailedListV3RequestFieldsItem(enum.StrEnum):
    AVAILABLE_SPACES = "available_spaces"
    CAPACITY = "capacity"
    CLOSED_SPACES = "closed_spaces"
    ENROLLED = "enrolled"
    IS_OVER_ENROLLED = "is_over_enrolled"
    OCCUPANCY_RATE = "occupancy_rate"
    OCCUPIED_SPACES = "occupied_spaces"
    OPEN_SPACES = "open_spaces"
    PERIOD = "period"
    ROOM_ID = "room_id"
    ROOM_NAME = "room_name"
    SCHOOL_ID = "school_id"
    SCHOOL_NAME = "school_name"
    UNAVAILABLE_SPACES = "unavailable_spaces"

    def visit(
        self,
        available_spaces: typing.Callable[[], T_Result],
        capacity: typing.Callable[[], T_Result],
        closed_spaces: typing.Callable[[], T_Result],
        enrolled: typing.Callable[[], T_Result],
        is_over_enrolled: typing.Callable[[], T_Result],
        occupancy_rate: typing.Callable[[], T_Result],
        occupied_spaces: typing.Callable[[], T_Result],
        open_spaces: typing.Callable[[], T_Result],
        period: typing.Callable[[], T_Result],
        room_id: typing.Callable[[], T_Result],
        room_name: typing.Callable[[], T_Result],
        school_id: typing.Callable[[], T_Result],
        school_name: typing.Callable[[], T_Result],
        unavailable_spaces: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetSpacesDetailedListV3RequestFieldsItem.AVAILABLE_SPACES:
            return available_spaces()
        if self is GetSpacesDetailedListV3RequestFieldsItem.CAPACITY:
            return capacity()
        if self is GetSpacesDetailedListV3RequestFieldsItem.CLOSED_SPACES:
            return closed_spaces()
        if self is GetSpacesDetailedListV3RequestFieldsItem.ENROLLED:
            return enrolled()
        if self is GetSpacesDetailedListV3RequestFieldsItem.IS_OVER_ENROLLED:
            return is_over_enrolled()
        if self is GetSpacesDetailedListV3RequestFieldsItem.OCCUPANCY_RATE:
            return occupancy_rate()
        if self is GetSpacesDetailedListV3RequestFieldsItem.OCCUPIED_SPACES:
            return occupied_spaces()
        if self is GetSpacesDetailedListV3RequestFieldsItem.OPEN_SPACES:
            return open_spaces()
        if self is GetSpacesDetailedListV3RequestFieldsItem.PERIOD:
            return period()
        if self is GetSpacesDetailedListV3RequestFieldsItem.ROOM_ID:
            return room_id()
        if self is GetSpacesDetailedListV3RequestFieldsItem.ROOM_NAME:
            return room_name()
        if self is GetSpacesDetailedListV3RequestFieldsItem.SCHOOL_ID:
            return school_id()
        if self is GetSpacesDetailedListV3RequestFieldsItem.SCHOOL_NAME:
            return school_name()
        if self is GetSpacesDetailedListV3RequestFieldsItem.UNAVAILABLE_SPACES:
            return unavailable_spaces()
