

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V60BaseRateJurType(enum.StrEnum):
    """
    Jurisdiction level combined with the tax kind (sales vs use) this component represents.
    """

    US_STATE_SALES_TAX = "US_STATE_SALES_TAX"
    US_STATE_USE_TAX = "US_STATE_USE_TAX"
    US_COUNTY_SALES_TAX = "US_COUNTY_SALES_TAX"
    US_COUNTY_USE_TAX = "US_COUNTY_USE_TAX"
    US_CITY_SALES_TAX = "US_CITY_SALES_TAX"
    US_CITY_USE_TAX = "US_CITY_USE_TAX"
    US_DISTRICT_SALES_TAX = "US_DISTRICT_SALES_TAX"
    US_DISTRICT_USE_TAX = "US_DISTRICT_USE_TAX"

    def visit(
        self,
        us_state_sales_tax: typing.Callable[[], T_Result],
        us_state_use_tax: typing.Callable[[], T_Result],
        us_county_sales_tax: typing.Callable[[], T_Result],
        us_county_use_tax: typing.Callable[[], T_Result],
        us_city_sales_tax: typing.Callable[[], T_Result],
        us_city_use_tax: typing.Callable[[], T_Result],
        us_district_sales_tax: typing.Callable[[], T_Result],
        us_district_use_tax: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V60BaseRateJurType.US_STATE_SALES_TAX:
            return us_state_sales_tax()
        if self is V60BaseRateJurType.US_STATE_USE_TAX:
            return us_state_use_tax()
        if self is V60BaseRateJurType.US_COUNTY_SALES_TAX:
            return us_county_sales_tax()
        if self is V60BaseRateJurType.US_COUNTY_USE_TAX:
            return us_county_use_tax()
        if self is V60BaseRateJurType.US_CITY_SALES_TAX:
            return us_city_sales_tax()
        if self is V60BaseRateJurType.US_CITY_USE_TAX:
            return us_city_use_tax()
        if self is V60BaseRateJurType.US_DISTRICT_SALES_TAX:
            return us_district_sales_tax()
        if self is V60BaseRateJurType.US_DISTRICT_USE_TAX:
            return us_district_use_tax()
