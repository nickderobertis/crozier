

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BodyFieldsType(enum.StrEnum):
    MULTIPART = "MULTIPART"

    def visit(self, multipart: typing.Callable[[], T_Result]) -> T_Result:
        if self is BodyFieldsType.MULTIPART:
            return multipart()
