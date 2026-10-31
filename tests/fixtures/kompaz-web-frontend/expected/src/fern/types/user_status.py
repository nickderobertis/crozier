

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserStatus(enum.StrEnum):
    """
    Where a user is in the invitation lifecycle. Deliberately separate from deletion, which is recorded by its own timestamp: the status says how far somebody got, and overwriting it on delete would lose the answer a restore has to put back.
    | |
    |---|
    | `Invited` <br/> Invited, but has not yet signed in for the first time. |
    | `Active` <br/> Has proven ownership of their email address and can sign in. |
    """

    INVITED = "Invited"
    ACTIVE = "Active"

    def visit(self, invited: typing.Callable[[], T_Result], active: typing.Callable[[], T_Result]) -> T_Result:
        if self is UserStatus.INVITED:
            return invited()
        if self is UserStatus.ACTIVE:
            return active()
