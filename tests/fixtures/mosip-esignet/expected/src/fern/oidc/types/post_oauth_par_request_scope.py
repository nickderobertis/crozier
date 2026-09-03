

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostOauthParRequestScope(enum.StrEnum):
    """
    Specifies what access privileges are being requested for Access Tokens. The scopes associated with Access Tokens determine what resources will be available when they are used to access OAuth 2.0 protected endpoints. OpenID Connect requests MUST contain the OpenID scope value.
    """

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
        if self is PostOauthParRequestScope.OPENID:
            return openid()
        if self is PostOauthParRequestScope.PROFILE:
            return profile()
        if self is PostOauthParRequestScope.EMAIL:
            return email()
        if self is PostOauthParRequestScope.ADDRESS:
            return address()
        if self is PostOauthParRequestScope.PHONE:
            return phone()
        if self is PostOauthParRequestScope.OFFLINE_ACCESS:
            return offline_access()
