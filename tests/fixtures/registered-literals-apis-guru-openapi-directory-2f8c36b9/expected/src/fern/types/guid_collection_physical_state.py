

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GuidCollectionPhysicalState(enum.StrEnum):
    """
    Physical attachment state of the collection
    """

    UNATTACHED = "UNATTACHED"
    ATTACHED = "ATTACHED"
    DETACHED = "DETACHED"

    def visit(
        self,
        unattached: typing.Callable[[], T_Result],
        attached: typing.Callable[[], T_Result],
        detached: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GuidCollectionPhysicalState.UNATTACHED:
            return unattached()
        if self is GuidCollectionPhysicalState.ATTACHED:
            return attached()
        if self is GuidCollectionPhysicalState.DETACHED:
            return detached()
