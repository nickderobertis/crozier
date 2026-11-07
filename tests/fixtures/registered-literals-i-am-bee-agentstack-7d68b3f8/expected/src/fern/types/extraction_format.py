

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtractionFormat(enum.StrEnum):
    MARKDOWN = "markdown"
    VENDOR_SPECIFIC_JSON = "vendor_specific_json"

    def visit(
        self, markdown: typing.Callable[[], T_Result], vendor_specific_json: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is ExtractionFormat.MARKDOWN:
            return markdown()
        if self is ExtractionFormat.VENDOR_SPECIFIC_JSON:
            return vendor_specific_json()
