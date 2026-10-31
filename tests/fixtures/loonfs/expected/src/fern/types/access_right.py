

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccessRight(enum.StrEnum):
    """
    One right that a grant can include.
    """

    READ = "read"
    HISTORY = "history"
    WRITE = "write"
    CREATE = "create"
    REMOVE = "remove"
    SHARE = "share"
    MANAGE = "manage"
    ADMIN = "admin"

    def visit(
        self,
        read: typing.Callable[[], T_Result],
        history: typing.Callable[[], T_Result],
        write: typing.Callable[[], T_Result],
        create: typing.Callable[[], T_Result],
        remove: typing.Callable[[], T_Result],
        share: typing.Callable[[], T_Result],
        manage: typing.Callable[[], T_Result],
        admin: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AccessRight.READ:
            return read()
        if self is AccessRight.HISTORY:
            return history()
        if self is AccessRight.WRITE:
            return write()
        if self is AccessRight.CREATE:
            return create()
        if self is AccessRight.REMOVE:
            return remove()
        if self is AccessRight.SHARE:
            return share()
        if self is AccessRight.MANAGE:
            return manage()
        if self is AccessRight.ADMIN:
            return admin()
