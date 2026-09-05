

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PricingConfigurationTradePolicyConfigsItem(UniversalBaseModel):
    minimum_markup: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="minimumMarkup"),
        pydantic.Field(alias="minimumMarkup", description="Trade Policy Minimum Markup."),
    ] = None
    """
    Trade Policy Minimum Markup.
    """

    rules_should_affect_list_price: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="rulesShouldAffectListPrice"),
        pydantic.Field(
            alias="rulesShouldAffectListPrice",
            description="Defines if the Price Rule should affect the list price too.",
        ),
    ] = None
    """
    Defines if the Price Rule should affect the list price too.
    """

    trade_policy_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="tradePolicyId"),
        pydantic.Field(alias="tradePolicyId", description="Trade Policy ID."),
    ] = None
    """
    Trade Policy ID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
