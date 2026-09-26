

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocFormsGet200ResponseFieldsItemUnknownOrigin(enum.StrEnum):
    ACROFORM = "acroform"
    RECOVERED = "recovered"

    def visit(self, acroform: typing.Callable[[], T_Result], recovered: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocFormsGet200ResponseFieldsItemUnknownOrigin.ACROFORM:
            return acroform()
        if self is DocFormsGet200ResponseFieldsItemUnknownOrigin.RECOVERED:
            return recovered()
