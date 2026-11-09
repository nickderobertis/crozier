

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .unofficial_currency_code_list import UnofficialCurrencyCodeList


class StandaloneCurrencyCodeList(UniversalBaseModel):
    """
    The following currency codes are supported by Plaid.
    """

    iso_currency_code: str = pydantic.Field()
    """
    Plaid supports all ISO 4217 currency codes.
    """

    unofficial_currency_code: UnofficialCurrencyCodeList

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
