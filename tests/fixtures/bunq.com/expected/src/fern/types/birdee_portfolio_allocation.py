

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BirdeePortfolioAllocation(UniversalBaseModel):
    amount: typing.Optional[str] = pydantic.Field(default=None)
    """
    Monetary amount of the financial instrument in the portfolio.
    """

    instrument_asset_class: typing.Optional[str] = pydantic.Field(default=None)
    """
    Asset Class of the instrument.
    """

    instrument_asset_class_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the asset class.
    """

    instrument_currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    Currency of the instrument.
    """

    instrument_isin: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISIN code of the instrument.
    """

    instrument_key_information_document_uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    Key Information Document of the instrument.
    """

    instrument_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the instrument.
    """

    instrument_region_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the geographical region covered by the instrument
    """

    price: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unit price of the financial instrument.
    """

    quantity: typing.Optional[str] = pydantic.Field(default=None)
    """
    Quantity of the financial instrument in the portfolio.
    """

    weight: typing.Optional[str] = pydantic.Field(default=None)
    """
    Weight of the financial instrument in the model portfolio.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
