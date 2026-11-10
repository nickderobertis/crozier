

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ClientProvidedRawTransaction(UniversalBaseModel):
    """
    A client-provided transaction for Plaid to enhance.
    """

    amount: float = pydantic.Field()
    """
    The value of the transaction with direction. (NOTE: this will affect enrichment results, so directions are important):.
      Negative (-) for credits (e.g., incoming transfers, refunds)
      Positive (+) for debits (e.g., purchases, fees, outgoing transfers)
    """

    description: str = pydantic.Field()
    """
    The raw description of the transaction.
    """

    id: str = pydantic.Field()
    """
    A unique ID for the transaction used to help you tie data back to your systems.
    """

    iso_currency_code: str = pydantic.Field()
    """
    The ISO-4217 currency code of the transaction e.g. USD.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
