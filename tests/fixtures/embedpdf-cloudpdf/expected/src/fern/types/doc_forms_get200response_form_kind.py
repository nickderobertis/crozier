

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocFormsGet200ResponseFormKind(enum.StrEnum):
    NONE = "none"
    ACROFORM = "acroform"
    XFA = "xfa"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        acroform: typing.Callable[[], T_Result],
        xfa: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocFormsGet200ResponseFormKind.NONE:
            return none()
        if self is DocFormsGet200ResponseFormKind.ACROFORM:
            return acroform()
        if self is DocFormsGet200ResponseFormKind.XFA:
            return xfa()
