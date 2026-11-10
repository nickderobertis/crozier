

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .enrich_transaction_direction import EnrichTransactionDirection
from .enrichments import Enrichments


class ClientProvidedEnrichedTransaction(UniversalBaseModel):
    """
    A client-provided transaction that Plaid has enriched.
    """

    amount: float = pydantic.Field()
    """
    The absolute value of the transaction (>= 0)
    """

    description: str = pydantic.Field()
    """
    The raw description of the transaction.
    """

    direction: typing.Optional[EnrichTransactionDirection] = None
    enrichments: Enrichments
    id: str = pydantic.Field()
    """
    The unique ID for the transaction as provided by you in the request.
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
