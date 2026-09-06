

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EventConditionsFsEventsItem(enum.StrEnum):
    UPLOAD = "upload"
    DOWNLOAD = "download"
    DELETE = "delete"
    RENAME = "rename"
    MKDIR = "mkdir"
    RMDIR = "rmdir"
    COPY = "copy"
    SSH_CMD = "ssh_cmd"
    PRE_UPLOAD = "pre-upload"
    PRE_DOWNLOAD = "pre-download"
    PRE_DELETE = "pre-delete"
    FIRST_UPLOAD = "first-upload"
    FIRST_DOWNLOAD = "first-download"

    def visit(
        self,
        upload: typing.Callable[[], T_Result],
        download: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        rename: typing.Callable[[], T_Result],
        mkdir: typing.Callable[[], T_Result],
        rmdir: typing.Callable[[], T_Result],
        copy: typing.Callable[[], T_Result],
        ssh_cmd: typing.Callable[[], T_Result],
        pre_upload: typing.Callable[[], T_Result],
        pre_download: typing.Callable[[], T_Result],
        pre_delete: typing.Callable[[], T_Result],
        first_upload: typing.Callable[[], T_Result],
        first_download: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EventConditionsFsEventsItem.UPLOAD:
            return upload()
        if self is EventConditionsFsEventsItem.DOWNLOAD:
            return download()
        if self is EventConditionsFsEventsItem.DELETE:
            return delete()
        if self is EventConditionsFsEventsItem.RENAME:
            return rename()
        if self is EventConditionsFsEventsItem.MKDIR:
            return mkdir()
        if self is EventConditionsFsEventsItem.RMDIR:
            return rmdir()
        if self is EventConditionsFsEventsItem.COPY:
            return copy()
        if self is EventConditionsFsEventsItem.SSH_CMD:
            return ssh_cmd()
        if self is EventConditionsFsEventsItem.PRE_UPLOAD:
            return pre_upload()
        if self is EventConditionsFsEventsItem.PRE_DOWNLOAD:
            return pre_download()
        if self is EventConditionsFsEventsItem.PRE_DELETE:
            return pre_delete()
        if self is EventConditionsFsEventsItem.FIRST_UPLOAD:
            return first_upload()
        if self is EventConditionsFsEventsItem.FIRST_DOWNLOAD:
            return first_download()
