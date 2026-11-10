

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transactions_rule_details import TransactionsRuleDetails


class TransactionsCategoryRule(UniversalBaseModel):
    """
    A representation of a transactions category rule.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date and time when a rule was created in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DDTHH:mm:ssZ` ).
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier of the rule created
    """

    item_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier of the Item the rule was created for.
    """

    personal_finance_category: typing.Optional[str] = pydantic.Field(default=None)
    """
    Personal finance category unique identifier.
    
    In the personal finance category taxonomy, this field is represented by the detailed category field.
    """

    rule_details: typing.Optional[TransactionsRuleDetails] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
