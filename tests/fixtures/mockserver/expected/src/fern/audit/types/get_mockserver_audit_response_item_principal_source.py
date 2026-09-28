

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetMockserverAuditResponseItemPrincipalSource(enum.StrEnum):
    JWT = "jwt"
    MTLS = "mtls"
    NONE = "none"

    def visit(
        self,
        jwt: typing.Callable[[], T_Result],
        mtls: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetMockserverAuditResponseItemPrincipalSource.JWT:
            return jwt()
        if self is GetMockserverAuditResponseItemPrincipalSource.MTLS:
            return mtls()
        if self is GetMockserverAuditResponseItemPrincipalSource.NONE:
            return none()
