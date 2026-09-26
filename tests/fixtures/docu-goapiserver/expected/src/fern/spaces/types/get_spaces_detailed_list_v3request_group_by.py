

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSpacesDetailedListV3RequestGroupBy(enum.StrEnum):
    ROOM_ID = "room_id"
    ROOM_NAME = "room_name"
    SCHOOL_ID = "school_id"
    SCHOOL_NAME = "school_name"

    def visit(
        self,
        room_id: typing.Callable[[], T_Result],
        room_name: typing.Callable[[], T_Result],
        school_id: typing.Callable[[], T_Result],
        school_name: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetSpacesDetailedListV3RequestGroupBy.ROOM_ID:
            return room_id()
        if self is GetSpacesDetailedListV3RequestGroupBy.ROOM_NAME:
            return room_name()
        if self is GetSpacesDetailedListV3RequestGroupBy.SCHOOL_ID:
            return school_id()
        if self is GetSpacesDetailedListV3RequestGroupBy.SCHOOL_NAME:
            return school_name()
