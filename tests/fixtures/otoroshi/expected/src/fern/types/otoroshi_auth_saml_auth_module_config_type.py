

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OtoroshiAuthSamlAuthModuleConfigType(enum.StrEnum):
    """
    the type of the module
    """

    SAML = "saml"
    OAUTH1 = "oauth1"
    OAUTH2 = "oauth2"
    LDAP = "ldap"
    BASIC = "basic"

    def visit(
        self,
        saml: typing.Callable[[], T_Result],
        oauth1: typing.Callable[[], T_Result],
        oauth2: typing.Callable[[], T_Result],
        ldap: typing.Callable[[], T_Result],
        basic: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OtoroshiAuthSamlAuthModuleConfigType.SAML:
            return saml()
        if self is OtoroshiAuthSamlAuthModuleConfigType.OAUTH1:
            return oauth1()
        if self is OtoroshiAuthSamlAuthModuleConfigType.OAUTH2:
            return oauth2()
        if self is OtoroshiAuthSamlAuthModuleConfigType.LDAP:
            return ldap()
        if self is OtoroshiAuthSamlAuthModuleConfigType.BASIC:
            return basic()
