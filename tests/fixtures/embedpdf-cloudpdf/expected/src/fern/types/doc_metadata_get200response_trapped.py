

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocMetadataGet200ResponseTrapped(enum.StrEnum):
    TRUE = "true"
    FALSE = "false"
    UNKNOWN = "unknown"

    def visit(
        self,
        true: typing.Callable[[], T_Result],
        false: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocMetadataGet200ResponseTrapped.TRUE:
            return true()
        if self is DocMetadataGet200ResponseTrapped.FALSE:
            return false()
        if self is DocMetadataGet200ResponseTrapped.UNKNOWN:
            return unknown()
