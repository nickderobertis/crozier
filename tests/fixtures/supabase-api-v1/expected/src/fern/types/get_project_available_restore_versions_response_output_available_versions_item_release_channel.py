

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetProjectAvailableRestoreVersionsResponseOutputAvailableVersionsItemReleaseChannel(enum.StrEnum):
    INTERNAL = "internal"
    ALPHA = "alpha"
    BETA = "beta"
    GA = "ga"
    WITHDRAWN = "withdrawn"
    PREVIEW = "preview"

    def visit(
        self,
        internal: typing.Callable[[], T_Result],
        alpha: typing.Callable[[], T_Result],
        beta: typing.Callable[[], T_Result],
        ga: typing.Callable[[], T_Result],
        withdrawn: typing.Callable[[], T_Result],
        preview: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetProjectAvailableRestoreVersionsResponseOutputAvailableVersionsItemReleaseChannel.INTERNAL:
            return internal()
        if self is GetProjectAvailableRestoreVersionsResponseOutputAvailableVersionsItemReleaseChannel.ALPHA:
            return alpha()
        if self is GetProjectAvailableRestoreVersionsResponseOutputAvailableVersionsItemReleaseChannel.BETA:
            return beta()
        if self is GetProjectAvailableRestoreVersionsResponseOutputAvailableVersionsItemReleaseChannel.GA:
            return ga()
        if self is GetProjectAvailableRestoreVersionsResponseOutputAvailableVersionsItemReleaseChannel.WITHDRAWN:
            return withdrawn()
        if self is GetProjectAvailableRestoreVersionsResponseOutputAvailableVersionsItemReleaseChannel.PREVIEW:
            return preview()
