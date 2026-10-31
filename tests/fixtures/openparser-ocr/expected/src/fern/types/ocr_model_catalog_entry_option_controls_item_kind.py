

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OcrModelCatalogEntryOptionControlsItemKind(enum.StrEnum):
    BOOLEAN = "boolean"
    ENUM = "enum"
    NULLABLE_ENUM = "nullable-enum"
    NULLABLE_STRING = "nullable-string"
    NULLABLE_STRING_LIST = "nullable-string-list"

    def visit(
        self,
        boolean: typing.Callable[[], T_Result],
        enum: typing.Callable[[], T_Result],
        nullable_enum: typing.Callable[[], T_Result],
        nullable_string: typing.Callable[[], T_Result],
        nullable_string_list: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OcrModelCatalogEntryOptionControlsItemKind.BOOLEAN:
            return boolean()
        if self is OcrModelCatalogEntryOptionControlsItemKind.ENUM:
            return enum()
        if self is OcrModelCatalogEntryOptionControlsItemKind.NULLABLE_ENUM:
            return nullable_enum()
        if self is OcrModelCatalogEntryOptionControlsItemKind.NULLABLE_STRING:
            return nullable_string()
        if self is OcrModelCatalogEntryOptionControlsItemKind.NULLABLE_STRING_LIST:
            return nullable_string_list()
