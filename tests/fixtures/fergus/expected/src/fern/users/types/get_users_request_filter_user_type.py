

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetUsersRequestFilterUserType(enum.StrEnum):
    CONTRACTOR = "contractor"
    TIME_SHEET_ONLY = "time_sheet_only"
    FIELD_WORKER = "field_worker"
    APPRENTICE = "apprentice"
    TRADESMAN = "tradesman"
    ADVISOR = "advisor"
    FULL_USER = "full_user"

    def visit(
        self,
        contractor: typing.Callable[[], T_Result],
        time_sheet_only: typing.Callable[[], T_Result],
        field_worker: typing.Callable[[], T_Result],
        apprentice: typing.Callable[[], T_Result],
        tradesman: typing.Callable[[], T_Result],
        advisor: typing.Callable[[], T_Result],
        full_user: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetUsersRequestFilterUserType.CONTRACTOR:
            return contractor()
        if self is GetUsersRequestFilterUserType.TIME_SHEET_ONLY:
            return time_sheet_only()
        if self is GetUsersRequestFilterUserType.FIELD_WORKER:
            return field_worker()
        if self is GetUsersRequestFilterUserType.APPRENTICE:
            return apprentice()
        if self is GetUsersRequestFilterUserType.TRADESMAN:
            return tradesman()
        if self is GetUsersRequestFilterUserType.ADVISOR:
            return advisor()
        if self is GetUsersRequestFilterUserType.FULL_USER:
            return full_user()
