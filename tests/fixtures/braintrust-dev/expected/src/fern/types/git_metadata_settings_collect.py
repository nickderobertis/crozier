

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GitMetadataSettingsCollect(enum.StrEnum):
    ALL = "all"
    NONE = "none"
    SOME = "some"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
        some: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GitMetadataSettingsCollect.ALL:
            return all_()
        if self is GitMetadataSettingsCollect.NONE:
            return none()
        if self is GitMetadataSettingsCollect.SOME:
            return some()
