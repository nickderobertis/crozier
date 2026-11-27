

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ManifestSecureTextScalarConfigType(enum.StrEnum):
    SECURE_TEXT = "secure_text"

    def visit(self, secure_text: typing.Callable[[], T_Result]) -> T_Result:
        if self is ManifestSecureTextScalarConfigType.SECURE_TEXT:
            return secure_text()
