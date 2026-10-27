

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChannelRequestExpand(enum.StrEnum):
    MEMBERS = "members"
    TABS = "tabs"
    FILES_FOLDER = "filesFolder"

    def visit(
        self,
        members: typing.Callable[[], T_Result],
        tabs: typing.Callable[[], T_Result],
        files_folder: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChannelRequestExpand.MEMBERS:
            return members()
        if self is GetChannelRequestExpand.TABS:
            return tabs()
        if self is GetChannelRequestExpand.FILES_FOLDER:
            return files_folder()
