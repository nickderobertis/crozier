

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentType(enum.StrEnum):
    PLATFORM_FILE = "platform_file"
    EXTERNAL = "external"

    def visit(self, platform_file: typing.Callable[[], T_Result], external: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocumentType.PLATFORM_FILE:
            return platform_file()
        if self is DocumentType.EXTERNAL:
            return external()
