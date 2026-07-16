

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObExternalPartyType1Code(enum.StrEnum):
    """
    Party type, in a coded form.
    """

    DELEGATE = "Delegate"
    JOINT = "Joint"
    SOLE = "Sole"

    def visit(
        self,
        delegate: typing.Callable[[], T_Result],
        joint: typing.Callable[[], T_Result],
        sole: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObExternalPartyType1Code.DELEGATE:
            return delegate()
        if self is ObExternalPartyType1Code.JOINT:
            return joint()
        if self is ObExternalPartyType1Code.SOLE:
            return sole()
