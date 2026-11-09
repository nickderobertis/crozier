

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_provided_enhanced_transaction import ClientProvidedEnhancedTransaction


class TransactionsEnhanceGetResponse(UniversalBaseModel):
    """
    TransactionsEnhanceGetResponse defines the response schema for `/beta/transactions/v1/enhance`.
    """

    enhanced_transactions: typing.List[ClientProvidedEnhancedTransaction] = pydantic.Field()
    """
    An array of enhanced transactions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
