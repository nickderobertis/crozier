

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BodyTenType(enum.StrEnum):
    XML_SCHEMA = "XML_SCHEMA"

    def visit(self, xml_schema: typing.Callable[[], T_Result]) -> T_Result:
        if self is BodyTenType.XML_SCHEMA:
            return xml_schema()
