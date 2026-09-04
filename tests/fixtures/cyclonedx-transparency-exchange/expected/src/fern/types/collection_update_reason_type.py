

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CollectionUpdateReasonType(enum.StrEnum):
    """
    Type of TEA collection update
    """

    INITIAL_RELEASE = "INITIAL_RELEASE"
    VEX_UPDATED = "VEX_UPDATED"
    ARTIFACT_UPDATED = "ARTIFACT_UPDATED"
    ARTIFACT_ADDED = "ARTIFACT_ADDED"
    ARTIFACT_REMOVED = "ARTIFACT_REMOVED"

    def visit(
        self,
        initial_release: typing.Callable[[], T_Result],
        vex_updated: typing.Callable[[], T_Result],
        artifact_updated: typing.Callable[[], T_Result],
        artifact_added: typing.Callable[[], T_Result],
        artifact_removed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CollectionUpdateReasonType.INITIAL_RELEASE:
            return initial_release()
        if self is CollectionUpdateReasonType.VEX_UPDATED:
            return vex_updated()
        if self is CollectionUpdateReasonType.ARTIFACT_UPDATED:
            return artifact_updated()
        if self is CollectionUpdateReasonType.ARTIFACT_ADDED:
            return artifact_added()
        if self is CollectionUpdateReasonType.ARTIFACT_REMOVED:
            return artifact_removed()
