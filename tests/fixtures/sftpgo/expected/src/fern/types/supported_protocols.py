

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SupportedProtocols(enum.StrEnum):
    """
    Protocols:
      * `SSH` - includes both SFTP and SSH commands
      * `FTP` - plain FTP and FTPES/FTPS
      * `DAV` - WebDAV over HTTP/HTTPS
      * `HTTP` - WebClient/REST API
    """

    SSH = "SSH"
    FTP = "FTP"
    DAV = "DAV"
    HTTP = "HTTP"

    def visit(
        self,
        ssh: typing.Callable[[], T_Result],
        ftp: typing.Callable[[], T_Result],
        dav: typing.Callable[[], T_Result],
        http: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SupportedProtocols.SSH:
            return ssh()
        if self is SupportedProtocols.FTP:
            return ftp()
        if self is SupportedProtocols.DAV:
            return dav()
        if self is SupportedProtocols.HTTP:
            return http()
