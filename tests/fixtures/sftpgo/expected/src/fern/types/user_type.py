

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserType(enum.StrEnum):
    """
    This is an hint for authentication plugins. It is ignored when using SFTPGo internal authentication
    """

    EMPTY = ""
    LDAP_USER = "LDAPUser"
    OS_USER = "OSUser"

    def visit(
        self,
        empty: typing.Callable[[], T_Result],
        ldap_user: typing.Callable[[], T_Result],
        os_user: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UserType.EMPTY:
            return empty()
        if self is UserType.LDAP_USER:
            return ldap_user()
        if self is UserType.OS_USER:
            return os_user()
