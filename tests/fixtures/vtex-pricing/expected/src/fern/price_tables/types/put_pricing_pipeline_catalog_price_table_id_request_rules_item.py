

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .put_pricing_pipeline_catalog_price_table_id_request_rules_item_context import (
    PutPricingPipelineCatalogPriceTableIdRequestRulesItemContext,
)


class PutPricingPipelineCatalogPriceTableIdRequestRulesItem(UniversalBaseModel):
    """
    Object containing a price table rule.
    """

    context: PutPricingPipelineCatalogPriceTableIdRequestRulesItemContext = pydantic.Field()
    """
    Rule Context is a group of filters to be checked at an item level when applying the rule. If all those filters check out, the rule will be applied for that item, unless there is a fixed price for that item.
    """

    id: int = pydantic.Field()
    """
    Rule ID.
    """

    percentual_modifier: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="percentualModifier"),
        pydantic.Field(alias="percentualModifier", description="Percentual modifier."),
    ]
    """
    Percentual modifier.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
