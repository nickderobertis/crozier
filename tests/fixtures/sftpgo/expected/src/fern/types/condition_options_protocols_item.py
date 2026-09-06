

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConditionOptionsProtocolsItem(enum.StrEnum):
    SFTP = "SFTP"
    SCP = "SCP"
    SSH = "SSH"
    FTP = "FTP"
    DAV = "DAV"
    HTTP = "HTTP"
    HTTP_SHARE = "HTTPShare"
    OIDC = "OIDC"

    def visit(
        self,
        sftp: typing.Callable[[], T_Result],
        scp: typing.Callable[[], T_Result],
        ssh: typing.Callable[[], T_Result],
        ftp: typing.Callable[[], T_Result],
        dav: typing.Callable[[], T_Result],
        http: typing.Callable[[], T_Result],
        http_share: typing.Callable[[], T_Result],
        oidc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConditionOptionsProtocolsItem.SFTP:
            return sftp()
        if self is ConditionOptionsProtocolsItem.SCP:
            return scp()
        if self is ConditionOptionsProtocolsItem.SSH:
            return ssh()
        if self is ConditionOptionsProtocolsItem.FTP:
            return ftp()
        if self is ConditionOptionsProtocolsItem.DAV:
            return dav()
        if self is ConditionOptionsProtocolsItem.HTTP:
            return http()
        if self is ConditionOptionsProtocolsItem.HTTP_SHARE:
            return http_share()
        if self is ConditionOptionsProtocolsItem.OIDC:
            return oidc()
