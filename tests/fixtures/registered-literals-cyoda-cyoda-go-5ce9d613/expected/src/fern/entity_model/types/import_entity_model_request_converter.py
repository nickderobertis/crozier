

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ImportEntityModelRequestConverter(enum.StrEnum):
    SAMPLE_DATA = "SAMPLE_DATA"
    JSON_SCHEMA = "JSON_SCHEMA"
    SIMPLE_VIEW = "SIMPLE_VIEW"

    def visit(
        self,
        sample_data: typing.Callable[[], T_Result],
        json_schema: typing.Callable[[], T_Result],
        simple_view: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ImportEntityModelRequestConverter.SAMPLE_DATA:
            return sample_data()
        if self is ImportEntityModelRequestConverter.JSON_SCHEMA:
            return json_schema()
        if self is ImportEntityModelRequestConverter.SIMPLE_VIEW:
            return simple_view()
