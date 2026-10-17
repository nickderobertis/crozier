

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateBranchBodyReleaseChannel(enum.StrEnum):
    """
    Release channel. If not provided, GA will be used.
    """

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
        if self is CreateBranchBodyReleaseChannel.INTERNAL:
            return internal()
        if self is CreateBranchBodyReleaseChannel.ALPHA:
            return alpha()
        if self is CreateBranchBodyReleaseChannel.BETA:
            return beta()
        if self is CreateBranchBodyReleaseChannel.GA:
            return ga()
        if self is CreateBranchBodyReleaseChannel.WITHDRAWN:
            return withdrawn()
        if self is CreateBranchBodyReleaseChannel.PREVIEW:
            return preview()
