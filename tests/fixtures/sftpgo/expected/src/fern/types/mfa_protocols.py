

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MfaProtocols(enum.StrEnum):
    """
    Protocols:
      * `SSH` - includes both SFTP and SSH commands
      * `FTP` - plain FTP and FTPES/FTPS
      * `HTTP` - WebClient/REST API
    """

    SSH = "SSH"
    FTP = "FTP"
    HTTP = "HTTP"

    def visit(
        self,
        ssh: typing.Callable[[], T_Result],
        ftp: typing.Callable[[], T_Result],
        http: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MfaProtocols.SSH:
            return ssh()
        if self is MfaProtocols.FTP:
            return ftp()
        if self is MfaProtocols.HTTP:
            return http()
