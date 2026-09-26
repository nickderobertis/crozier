

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetBillingPlansV3RequestGroupBy(enum.StrEnum):
    SCHOOL_ID = "school_id"
    SCHOOL_NAME = "school_name"
    ROOM_ID = "room_id"
    ROOM_NAME = "room_name"

    def visit(
        self,
        school_id: typing.Callable[[], T_Result],
        school_name: typing.Callable[[], T_Result],
        room_id: typing.Callable[[], T_Result],
        room_name: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetBillingPlansV3RequestGroupBy.SCHOOL_ID:
            return school_id()
        if self is GetBillingPlansV3RequestGroupBy.SCHOOL_NAME:
            return school_name()
        if self is GetBillingPlansV3RequestGroupBy.ROOM_ID:
            return room_id()
        if self is GetBillingPlansV3RequestGroupBy.ROOM_NAME:
            return room_name()
