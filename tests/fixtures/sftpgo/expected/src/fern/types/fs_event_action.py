

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FsEventAction(enum.StrEnum):
    DOWNLOAD = "download"
    UPLOAD = "upload"
    FIRST_UPLOAD = "first-upload"
    FIRST_DOWNLOAD = "first-download"
    DELETE = "delete"
    RENAME = "rename"
    MKDIR = "mkdir"
    RMDIR = "rmdir"
    SSH_CMD = "ssh_cmd"

    def visit(
        self,
        download: typing.Callable[[], T_Result],
        upload: typing.Callable[[], T_Result],
        first_upload: typing.Callable[[], T_Result],
        first_download: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        rename: typing.Callable[[], T_Result],
        mkdir: typing.Callable[[], T_Result],
        rmdir: typing.Callable[[], T_Result],
        ssh_cmd: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FsEventAction.DOWNLOAD:
            return download()
        if self is FsEventAction.UPLOAD:
            return upload()
        if self is FsEventAction.FIRST_UPLOAD:
            return first_upload()
        if self is FsEventAction.FIRST_DOWNLOAD:
            return first_download()
        if self is FsEventAction.DELETE:
            return delete()
        if self is FsEventAction.RENAME:
            return rename()
        if self is FsEventAction.MKDIR:
            return mkdir()
        if self is FsEventAction.RMDIR:
            return rmdir()
        if self is FsEventAction.SSH_CMD:
            return ssh_cmd()
