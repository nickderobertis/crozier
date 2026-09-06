

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .create_sku_products_request_skus_item_field_data_compare_at_price import (
    CreateSkuProductsRequestSkusItemFieldDataCompareAtPrice,
)
from .create_sku_products_request_skus_item_field_data_ec_sku_billing_method import (
    CreateSkuProductsRequestSkusItemFieldDataEcSkuBillingMethod,
)
from .create_sku_products_request_skus_item_field_data_ec_sku_subscription_plan import (
    CreateSkuProductsRequestSkusItemFieldDataEcSkuSubscriptionPlan,
)
from .create_sku_products_request_skus_item_field_data_price import CreateSkuProductsRequestSkusItemFieldDataPrice
from .create_sku_products_request_skus_item_field_data_sku_properties_item import (
    CreateSkuProductsRequestSkusItemFieldDataSkuPropertiesItem,
)


class CreateSkuProductsRequestSkusItemFieldData(UniversalBaseModel):
    """
    Standard and Custom fields for a SKU
    """

    sku_values: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="sku-values"),
        pydantic.Field(
            alias="sku-values",
            description='A mapping between SKU properties and their values, represented as key-value pairs. Each key represents a SKU Property ID (e.g. "color") and maps to its corresponding SKU Value ID (e.g. "blue"). This structure defines the specific variant combination for a SKU.',
        ),
    ] = None
    """
    A mapping between SKU properties and their values, represented as key-value pairs. Each key represents a SKU Property ID (e.g. "color") and maps to its corresponding SKU Value ID (e.g. "blue"). This structure defines the specific variant combination for a SKU.
    """

    name: str = pydantic.Field()
    """
    Name of the Product
    """

    slug: str = pydantic.Field()
    """
    URL structure of the Product in your site.
    """

    price: CreateSkuProductsRequestSkusItemFieldDataPrice = pydantic.Field()
    """
    price of SKU
    """

    compare_at_price: typing_extensions.Annotated[
        typing.Optional[CreateSkuProductsRequestSkusItemFieldDataCompareAtPrice],
        FieldMetadata(alias="compare-at-price"),
        pydantic.Field(alias="compare-at-price", description="comparison price of SKU"),
    ] = None
    """
    comparison price of SKU
    """

    ec_sku_billing_method: typing_extensions.Annotated[
        typing.Optional[CreateSkuProductsRequestSkusItemFieldDataEcSkuBillingMethod],
        FieldMetadata(alias="ec-sku-billing-method"),
        pydantic.Field(
            alias="ec-sku-billing-method",
            description="[Billing method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for the SKU",
        ),
    ] = None
    """
    [Billing method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for the SKU
    """

    ec_sku_subscription_plan: typing_extensions.Annotated[
        typing.Optional[CreateSkuProductsRequestSkusItemFieldDataEcSkuSubscriptionPlan],
        FieldMetadata(alias="ec-sku-subscription-plan"),
        pydantic.Field(
            alias="ec-sku-subscription-plan",
            description="[Subscription plan](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#subscription) for the SKU",
        ),
    ] = None
    """
    [Subscription plan](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#subscription) for the SKU
    """

    main_image: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="main-image"),
        pydantic.Field(alias="main-image", description="The URL for the main image of the SKU"),
    ] = None
    """
    The URL for the main image of the SKU
    """

    sku: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for the SKU
    """

    sku_properties: typing_extensions.Annotated[
        typing.Optional[typing.List[CreateSkuProductsRequestSkusItemFieldDataSkuPropertiesItem]],
        FieldMetadata(alias="sku-properties"),
        pydantic.Field(alias="sku-properties", description="The properties of the SKU"),
    ] = None
    """
    The properties of the SKU
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
