

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_provided_transaction_location import ClientProvidedTransactionLocation
from .enrich_transaction_direction import EnrichTransactionDirection


class ClientProvidedTransaction(UniversalBaseModel):
    """
    A client-provided transaction for Plaid to enrich.
    """

    amount: float = pydantic.Field()
    """
    The absolute value of the transaction (>= 0). When testing Enrich, note that `amount` data should be realistic. Unrealistic or inaccurate `amount` data may result in reduced quality output.
    """

    date_posted: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date the transaction posted, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format.
    """

    description: str = pydantic.Field()
    """
    The raw description of the transaction. If you have location data in available an unstructured format, it may be appended to the `description` field.
    """

    direction: EnrichTransactionDirection
    id: str = pydantic.Field()
    """
    A unique ID for the transaction used to help you tie data back to your systems.
    """

    iso_currency_code: str = pydantic.Field()
    """
    The ISO-4217 currency code of the transaction e.g. USD.
    """

    location: typing.Optional[ClientProvidedTransactionLocation] = None
    mcc: typing.Optional[str] = pydantic.Field(default=None)
    """
    Merchant category codes (MCCs) are four-digit numbers that describe a merchant's primary business activities.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
