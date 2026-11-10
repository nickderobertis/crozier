

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transactions_rule_field import TransactionsRuleField
from .transactions_rule_type import TransactionsRuleType


class TransactionsRuleDetails(UniversalBaseModel):
    """
    A representation of transactions rule details.
    """

    field: TransactionsRuleField
    query: str = pydantic.Field()
    """
    For TRANSACTION_ID field, provide transaction_id. For NAME field, provide a string pattern.
    """

    type: TransactionsRuleType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
