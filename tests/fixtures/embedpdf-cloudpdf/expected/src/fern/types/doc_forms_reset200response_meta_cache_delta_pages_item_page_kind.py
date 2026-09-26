

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocFormsReset200ResponseMetaCacheDeltaPagesItemPageKind(enum.StrEnum):
    OBJECT_NUMBER = "objectNumber"

    def visit(self, object_number: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocFormsReset200ResponseMetaCacheDeltaPagesItemPageKind.OBJECT_NUMBER:
            return object_number()
