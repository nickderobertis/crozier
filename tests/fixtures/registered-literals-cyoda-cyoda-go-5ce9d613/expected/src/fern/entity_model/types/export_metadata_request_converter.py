

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ExportMetadataRequestConverter(enum.StrEnum):
    JSON_SCHEMA = "JSON_SCHEMA"
    SIMPLE_VIEW = "SIMPLE_VIEW"

    def visit(self, json_schema: typing.Callable[[], T_Result], simple_view: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExportMetadataRequestConverter.JSON_SCHEMA:
            return json_schema()
        if self is ExportMetadataRequestConverter.SIMPLE_VIEW:
            return simple_view()
