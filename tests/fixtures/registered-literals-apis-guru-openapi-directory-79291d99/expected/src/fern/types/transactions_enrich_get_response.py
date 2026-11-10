

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_provided_enriched_transaction import ClientProvidedEnrichedTransaction
from .request_id import RequestId


class TransactionsEnrichGetResponse(UniversalBaseModel):
    """
    TransactionsEnrichGetResponse defines the response schema for `/transactions/enrich`.
    """

    enriched_transactions: typing.List[ClientProvidedEnrichedTransaction] = pydantic.Field()
    """
    A list of enriched transactions.
    """

    request_id: typing.Optional[RequestId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
