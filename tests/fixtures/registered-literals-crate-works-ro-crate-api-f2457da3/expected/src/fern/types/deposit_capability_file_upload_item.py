

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DepositCapabilityFileUploadItem(enum.StrEnum):
    INLINE = "inline"
    PRESIGNED = "presigned"

    def visit(self, inline: typing.Callable[[], T_Result], presigned: typing.Callable[[], T_Result]) -> T_Result:
        if self is DepositCapabilityFileUploadItem.INLINE:
            return inline()
        if self is DepositCapabilityFileUploadItem.PRESIGNED:
            return presigned()
