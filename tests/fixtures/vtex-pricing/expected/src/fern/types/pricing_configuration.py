

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pricing_configuration_price_variation import PricingConfigurationPriceVariation
from .pricing_configuration_trade_policy_configs_item import PricingConfigurationTradePolicyConfigsItem


class PricingConfiguration(UniversalBaseModel):
    block_account: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="blockAccount"),
        pydantic.Field(
            alias="blockAccount", description="Defines if access to the Pricing APIs is blocked for external requests."
        ),
    ] = None
    """
    Defines if access to the Pricing APIs is blocked for external requests.
    """

    blocked_routes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="blockedRoutes"),
        pydantic.Field(alias="blockedRoutes", description="Array with all blocked routes."),
    ] = None
    """
    Array with all blocked routes.
    """

    default_markup: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="defaultMarkup"),
        pydantic.Field(alias="defaultMarkup", description="Account default markup."),
    ]
    """
    Account default markup.
    """

    has_migrated: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="hasMigrated"),
        pydantic.Field(alias="hasMigrated", description="Defines if the account has migrated to Pricing V2."),
    ]
    """
    Defines if the account has migrated to Pricing V2.
    """

    has_optional_base_price: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasOptionalBasePrice"),
        pydantic.Field(alias="hasOptionalBasePrice", description="Defines if optional base price is allowed."),
    ] = None
    """
    Defines if optional base price is allowed.
    """

    has_price_inheritance: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasPriceInheritance"),
        pydantic.Field(
            alias="hasPriceInheritance", description="Deprecated. Use the `priceInheritance` field instead."
        ),
    ] = None
    """
    Deprecated. Use the `priceInheritance` field instead.
    """

    migration_status: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="migrationStatus"),
        pydantic.Field(alias="migrationStatus", description="Pricing V2 migration status."),
    ] = None
    """
    Pricing V2 migration status.
    """

    minimum_markups: typing_extensions.Annotated[
        typing.Dict[str, int],
        FieldMetadata(alias="minimumMarkups"),
        pydantic.Field(alias="minimumMarkups", description="Account minimum markup."),
    ]
    """
    Account minimum markup.
    """

    price_inheritance: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="priceInheritance"),
        pydantic.Field(
            alias="priceInheritance",
            description="Condition of price inheritance from its parent account. This field can have three possible values: `never` if the store should never inherit prices, `nonexistent` if the store should only inherit prices in case of nonexistent prices for a given product, or `always` if the store should always inherit prices, regardless of its own prices.",
        ),
    ] = None
    """
    Condition of price inheritance from its parent account. This field can have three possible values: `never` if the store should never inherit prices, `nonexistent` if the store should only inherit prices in case of nonexistent prices for a given product, or `always` if the store should always inherit prices, regardless of its own prices.
    """

    price_table_limit: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="priceTableLimit"),
        pydantic.Field(alias="priceTableLimit", description="Price Table Limit."),
    ] = None
    """
    Price Table Limit.
    """

    price_table_selection_strategy: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="priceTableSelectionStrategy"),
        pydantic.Field(
            alias="priceTableSelectionStrategy",
            description="The strategy used to get prices when there is more than one option. Possible values: `first`, `highest`, `lowest`. Default: `first`.",
        ),
    ] = None
    """
    The strategy used to get prices when there is more than one option. Possible values: `first`, `highest`, `lowest`. Default: `first`.
    """

    price_variation: typing_extensions.Annotated[
        typing.Optional[PricingConfigurationPriceVariation],
        FieldMetadata(alias="priceVariation"),
        pydantic.Field(alias="priceVariation", description="Price Variation object."),
    ] = None
    """
    Price Variation object.
    """

    sellers_to_override: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Any]],
        FieldMetadata(alias="sellersToOverride"),
        pydantic.Field(alias="sellersToOverride", description="Overrides prices from sellers."),
    ] = None
    """
    Overrides prices from sellers.
    """

    trade_policy_configs: typing_extensions.Annotated[
        typing.Optional[typing.List[PricingConfigurationTradePolicyConfigsItem]],
        FieldMetadata(alias="tradePolicyConfigs"),
        pydantic.Field(alias="tradePolicyConfigs", description="Trade Policy Configurations array."),
    ] = None
    """
    Trade Policy Configurations array.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
