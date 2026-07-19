

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .currency_detail_peg import CurrencyDetailPeg


class CurrencyDetail(UniversalBaseModel):
    iso_code: str = pydantic.Field()
    """
    ISO 4217 currency code
    """

    iso_numeric: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO 4217 numeric code
    """

    name: str = pydantic.Field()
    """
    Full currency name
    """

    symbol: typing.Optional[str] = pydantic.Field(default=None)
    """
    Currency symbol
    """

    providers: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Provider keys that publish this currency
    """

    peg: typing.Optional[CurrencyDetailPeg] = pydantic.Field(default=None)
    """
    Peg metadata, present only for pegged currencies
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
