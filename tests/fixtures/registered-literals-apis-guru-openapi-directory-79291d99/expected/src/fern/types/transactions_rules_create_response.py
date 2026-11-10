

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId
from .transactions_category_rule import TransactionsCategoryRule


class TransactionsRulesCreateResponse(UniversalBaseModel):
    """
    TransactionsRulesCreateResponse defines the response schema for `/beta/transactions/rules/v1/create`
    """

    request_id: RequestId
    rule: TransactionsCategoryRule

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
