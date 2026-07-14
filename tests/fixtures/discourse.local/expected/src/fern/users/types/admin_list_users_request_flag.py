

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AdminListUsersRequestFlag(str, enum.Enum):
    ACTIVE = "active"
    NEW = "new"
    STAFF = "staff"
    SUSPENDED = "suspended"
    BLOCKED = "blocked"
    SUSPECT = "suspect"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        new: typing.Callable[[], T_Result],
        staff: typing.Callable[[], T_Result],
        suspended: typing.Callable[[], T_Result],
        blocked: typing.Callable[[], T_Result],
        suspect: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AdminListUsersRequestFlag.ACTIVE:
            return active()
        if self is AdminListUsersRequestFlag.NEW:
            return new()
        if self is AdminListUsersRequestFlag.STAFF:
            return staff()
        if self is AdminListUsersRequestFlag.SUSPENDED:
            return suspended()
        if self is AdminListUsersRequestFlag.BLOCKED:
            return blocked()
        if self is AdminListUsersRequestFlag.SUSPECT:
            return suspect()
