

import typing

V60BaseRateJurType = typing.Union[
    typing.Literal[
        "US_STATE_SALES_TAX",
        "US_STATE_USE_TAX",
        "US_COUNTY_SALES_TAX",
        "US_COUNTY_USE_TAX",
        "US_CITY_SALES_TAX",
        "US_CITY_USE_TAX",
        "US_DISTRICT_SALES_TAX",
        "US_DISTRICT_USE_TAX",
    ],
    typing.Any,
]
