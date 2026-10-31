

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtractionGroundingFieldTransformClaimOperation(enum.StrEnum):
    DATE_TIME_FORMAT = "date_time_format"
    NUMERIC_FORMAT = "numeric_format"
    QUANTITY_MAGNITUDE = "quantity_magnitude"
    UNIT_CONVERSION = "unit_conversion"
    CURRENCY_CODE = "currency_code"
    BOOLEAN_ALIAS = "boolean_alias"
    TEXT_NORMALIZATION = "text_normalization"
    ENUM_ALIAS = "enum_alias"

    def visit(
        self,
        date_time_format: typing.Callable[[], T_Result],
        numeric_format: typing.Callable[[], T_Result],
        quantity_magnitude: typing.Callable[[], T_Result],
        unit_conversion: typing.Callable[[], T_Result],
        currency_code: typing.Callable[[], T_Result],
        boolean_alias: typing.Callable[[], T_Result],
        text_normalization: typing.Callable[[], T_Result],
        enum_alias: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExtractionGroundingFieldTransformClaimOperation.DATE_TIME_FORMAT:
            return date_time_format()
        if self is ExtractionGroundingFieldTransformClaimOperation.NUMERIC_FORMAT:
            return numeric_format()
        if self is ExtractionGroundingFieldTransformClaimOperation.QUANTITY_MAGNITUDE:
            return quantity_magnitude()
        if self is ExtractionGroundingFieldTransformClaimOperation.UNIT_CONVERSION:
            return unit_conversion()
        if self is ExtractionGroundingFieldTransformClaimOperation.CURRENCY_CODE:
            return currency_code()
        if self is ExtractionGroundingFieldTransformClaimOperation.BOOLEAN_ALIAS:
            return boolean_alias()
        if self is ExtractionGroundingFieldTransformClaimOperation.TEXT_NORMALIZATION:
            return text_normalization()
        if self is ExtractionGroundingFieldTransformClaimOperation.ENUM_ALIAS:
            return enum_alias()
