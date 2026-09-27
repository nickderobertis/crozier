

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VersionStatusStatus(enum.StrEnum):
    """
    Explains what happened to this record between the previous release and the current release
    """

    ADDED = "added"
    UNCHANGED = "unchanged"
    UPDATED = "updated"

    def visit(
        self,
        added: typing.Callable[[], T_Result],
        unchanged: typing.Callable[[], T_Result],
        updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VersionStatusStatus.ADDED:
            return added()
        if self is VersionStatusStatus.UNCHANGED:
            return unchanged()
        if self is VersionStatusStatus.UPDATED:
            return updated()
