

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .getallpricetablesandrules_response_item_rules_item_context_date_range import (
    GetallpricetablesandrulesResponseItemRulesItemContextDateRange,
)
from .getallpricetablesandrules_response_item_rules_item_context_markup_range import (
    GetallpricetablesandrulesResponseItemRulesItemContextMarkupRange,
)


class GetallpricetablesandrulesResponseItemRulesItemContext(UniversalBaseModel):
    """
    Rule Context is a group of filters to be checked at an item level when applying the rule. If all those filters check out, the rule will be applied for that item, unless there is a fixed price for that item.
    """

    brands: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Brands that an item should have to be eligible for the rule. Format: key: `brandId`, value: `brandName`.
    """

    categories: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Categories that an item should have to be eligible for the rule. Format: key: `categoryId`, value: `categoryName`.
    """

    date_range: typing_extensions.Annotated[
        typing.Optional[GetallpricetablesandrulesResponseItemRulesItemContextDateRange],
        FieldMetadata(alias="dateRange"),
        pydantic.Field(alias="dateRange", description="The rule will be active during this time range."),
    ] = None
    """
    The rule will be active during this time range.
    """

    internal_categories: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="internalCategories"),
        pydantic.Field(alias="internalCategories", description="Internal Categories."),
    ] = None
    """
    Internal Categories.
    """

    markup_range: typing_extensions.Annotated[
        typing.Optional[GetallpricetablesandrulesResponseItemRulesItemContextMarkupRange],
        FieldMetadata(alias="markupRange"),
        pydantic.Field(
            alias="markupRange",
            description="For an item to be eligible to the rule, it's markup should be in this Markup Range.",
        ),
    ] = None
    """
    For an item to be eligible to the rule, it's markup should be in this Markup Range.
    """

    stock_statuses: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="stockStatuses"),
        pydantic.Field(alias="stockStatuses", description="Stock statuses."),
    ] = None
    """
    Stock statuses.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
