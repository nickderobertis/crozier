

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConnectionStatusProtocol(enum.StrEnum):
    SFTP = "SFTP"
    SCP = "SCP"
    SSH = "SSH"
    FTP = "FTP"
    DAV = "DAV"

    def visit(
        self,
        sftp: typing.Callable[[], T_Result],
        scp: typing.Callable[[], T_Result],
        ssh: typing.Callable[[], T_Result],
        ftp: typing.Callable[[], T_Result],
        dav: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConnectionStatusProtocol.SFTP:
            return sftp()
        if self is ConnectionStatusProtocol.SCP:
            return scp()
        if self is ConnectionStatusProtocol.SSH:
            return ssh()
        if self is ConnectionStatusProtocol.FTP:
            return ftp()
        if self is ConnectionStatusProtocol.DAV:
            return dav()
