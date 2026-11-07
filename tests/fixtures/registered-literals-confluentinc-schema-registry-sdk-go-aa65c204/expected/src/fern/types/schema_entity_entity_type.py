

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SchemaEntityEntityType(enum.StrEnum):
    SR_RECORD = "sr_record"
    SR_FIELD = "sr_field"

    def visit(self, sr_record: typing.Callable[[], T_Result], sr_field: typing.Callable[[], T_Result]) -> T_Result:
        if self is SchemaEntityEntityType.SR_RECORD:
            return sr_record()
        if self is SchemaEntityEntityType.SR_FIELD:
            return sr_field()
