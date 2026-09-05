

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .getallpricetablesandrules_response_item_rules_item_context import (
    GetallpricetablesandrulesResponseItemRulesItemContext,
)


class GetallpricetablesandrulesResponseItemRulesItem(UniversalBaseModel):
    """
    Object containing a price table rule.
    """

    context: typing.Optional[GetallpricetablesandrulesResponseItemRulesItemContext] = pydantic.Field(default=None)
    """
    Rule Context is a group of filters to be checked at an item level when applying the rule. If all those filters check out, the rule will be applied for that item, unless there is a fixed price for that item.
    """

    id: typing.Optional[float] = pydantic.Field(default=None)
    """
    Rule ID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
