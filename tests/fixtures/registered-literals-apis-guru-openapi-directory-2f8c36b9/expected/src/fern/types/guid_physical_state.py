

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GuidPhysicalState(enum.StrEnum):
    """
    Physical attachment state of the GUID
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
        if self is GuidPhysicalState.UNATTACHED:
            return unattached()
        if self is GuidPhysicalState.ATTACHED:
            return attached()
        if self is GuidPhysicalState.DETACHED:
            return detached()
