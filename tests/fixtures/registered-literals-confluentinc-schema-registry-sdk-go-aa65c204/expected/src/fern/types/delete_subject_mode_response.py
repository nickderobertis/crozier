

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteSubjectModeResponse(enum.StrEnum):
    READWRITE = "READWRITE"
    READONLY = "READONLY"
    READONLY_OVERRIDE = "READONLY_OVERRIDE"
    IMPORT = "IMPORT"

    def visit(
        self,
        readwrite: typing.Callable[[], T_Result],
        readonly: typing.Callable[[], T_Result],
        readonly_override: typing.Callable[[], T_Result],
        import_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeleteSubjectModeResponse.READWRITE:
            return readwrite()
        if self is DeleteSubjectModeResponse.READONLY:
            return readonly()
        if self is DeleteSubjectModeResponse.READONLY_OVERRIDE:
            return readonly_override()
        if self is DeleteSubjectModeResponse.IMPORT:
            return import_()
