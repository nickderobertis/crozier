

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Permission(enum.StrEnum):
    """
    Each permission permits a certain type of operation on an object in the system

    Permissions can be assigned to to objects on an individual basis, or grouped into roles
    """

    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"
    CREATE_ACLS = "create_acls"
    READ_ACLS = "read_acls"
    UPDATE_ACLS = "update_acls"
    DELETE_ACLS = "delete_acls"

    def visit(
        self,
        create: typing.Callable[[], T_Result],
        read: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        create_acls: typing.Callable[[], T_Result],
        read_acls: typing.Callable[[], T_Result],
        update_acls: typing.Callable[[], T_Result],
        delete_acls: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Permission.CREATE:
            return create()
        if self is Permission.READ:
            return read()
        if self is Permission.UPDATE:
            return update()
        if self is Permission.DELETE:
            return delete()
        if self is Permission.CREATE_ACLS:
            return create_acls()
        if self is Permission.READ_ACLS:
            return read_acls()
        if self is Permission.UPDATE_ACLS:
            return update_acls()
        if self is Permission.DELETE_ACLS:
            return delete_acls()
