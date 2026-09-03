

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAuthorizeRequestScope(enum.StrEnum):
    OPENID = "openid"
    PROFILE = "profile"
    EMAIL = "email"
    ADDRESS = "address"
    PHONE = "phone"
    OFFLINE_ACCESS = "offline_access"

    def visit(
        self,
        openid: typing.Callable[[], T_Result],
        profile: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        address: typing.Callable[[], T_Result],
        phone: typing.Callable[[], T_Result],
        offline_access: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetAuthorizeRequestScope.OPENID:
            return openid()
        if self is GetAuthorizeRequestScope.PROFILE:
            return profile()
        if self is GetAuthorizeRequestScope.EMAIL:
            return email()
        if self is GetAuthorizeRequestScope.ADDRESS:
            return address()
        if self is GetAuthorizeRequestScope.PHONE:
            return phone()
        if self is GetAuthorizeRequestScope.OFFLINE_ACCESS:
            return offline_access()
