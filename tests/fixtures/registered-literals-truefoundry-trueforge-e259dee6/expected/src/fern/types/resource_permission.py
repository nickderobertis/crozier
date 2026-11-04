

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResourcePermission(enum.StrEnum):
    """
    Granted action on a resource id or tenant entity kind.
    """

    USE = "USE"
    MANAGE = "MANAGE"
    DELETE = "DELETE"
    CREATE = "CREATE"

    def visit(
        self,
        use: typing.Callable[[], T_Result],
        manage: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        create: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ResourcePermission.USE:
            return use()
        if self is ResourcePermission.MANAGE:
            return manage()
        if self is ResourcePermission.DELETE:
            return delete()
        if self is ResourcePermission.CREATE:
            return create()
