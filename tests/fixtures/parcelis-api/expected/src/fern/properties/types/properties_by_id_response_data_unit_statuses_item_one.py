

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PropertiesByIdResponseDataUnitStatusesItemOne(enum.StrEnum):
    DRAFT = "draft"
    ACTIVE = "active"
    NOTICE = "notice"
    ENDED = "ended"

    def visit(
        self,
        draft: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        notice: typing.Callable[[], T_Result],
        ended: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PropertiesByIdResponseDataUnitStatusesItemOne.DRAFT:
            return draft()
        if self is PropertiesByIdResponseDataUnitStatusesItemOne.ACTIVE:
            return active()
        if self is PropertiesByIdResponseDataUnitStatusesItemOne.NOTICE:
            return notice()
        if self is PropertiesByIdResponseDataUnitStatusesItemOne.ENDED:
            return ended()
