

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UsersResponseDataItemUserType(enum.StrEnum):
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
        if self is UsersResponseDataItemUserType.CONTRACTOR:
            return contractor()
        if self is UsersResponseDataItemUserType.TIME_SHEET_ONLY:
            return time_sheet_only()
        if self is UsersResponseDataItemUserType.FIELD_WORKER:
            return field_worker()
        if self is UsersResponseDataItemUserType.APPRENTICE:
            return apprentice()
        if self is UsersResponseDataItemUserType.TRADESMAN:
            return tradesman()
        if self is UsersResponseDataItemUserType.ADVISOR:
            return advisor()
        if self is UsersResponseDataItemUserType.FULL_USER:
            return full_user()
