

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .ecomm_order_changed_payload_payload_purchased_items_item_row_total import (
    EcommOrderChangedPayloadPayloadPurchasedItemsItemRowTotal,
)
from .ecomm_order_changed_payload_payload_purchased_items_item_variant_image import (
    EcommOrderChangedPayloadPayloadPurchasedItemsItemVariantImage,
)
from .ecomm_order_changed_payload_payload_purchased_items_item_variant_price import (
    EcommOrderChangedPayloadPayloadPurchasedItemsItemVariantPrice,
)


class EcommOrderChangedPayloadPayloadPurchasedItemsItem(UniversalBaseModel):
    """
    An Item that was purchased
    """

    count: typing.Optional[float] = pydantic.Field(default=None)
    """
    Number of Item purchased.
    """

    row_total: typing_extensions.Annotated[
        typing.Optional[EcommOrderChangedPayloadPayloadPurchasedItemsItemRowTotal],
        FieldMetadata(alias="rowTotal"),
        pydantic.Field(alias="rowTotal", description="The total for the row"),
    ] = None
    """
    The total for the row
    """

    product_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="productId"),
        pydantic.Field(alias="productId", description="The unique identifier for the Product"),
    ] = None
    """
    The unique identifier for the Product
    """

    product_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="productName"),
        pydantic.Field(alias="productName", description="User-facing name of the Product"),
    ] = None
    """
    User-facing name of the Product
    """

    product_slug: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="productSlug"),
        pydantic.Field(alias="productSlug", description="Slug for the Product"),
    ] = None
    """
    Slug for the Product
    """

    variant_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="variantId"),
        pydantic.Field(alias="variantId", description="Identifier for the Product Variant (SKU)"),
    ] = None
    """
    Identifier for the Product Variant (SKU)
    """

    variant_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="variantName"),
        pydantic.Field(alias="variantName", description="User-facing name of the Product Variant (SKU)"),
    ] = None
    """
    User-facing name of the Product Variant (SKU)
    """

    variant_slug: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="variantSlug"),
        pydantic.Field(alias="variantSlug", description="Slug for the Product Variant (SKU)"),
    ] = None
    """
    Slug for the Product Variant (SKU)
    """

    variant_sku: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="variantSKU"),
        pydantic.Field(alias="variantSKU", description="The user-defined custom SKU of the Product Variant (SKU)"),
    ] = None
    """
    The user-defined custom SKU of the Product Variant (SKU)
    """

    variant_image: typing_extensions.Annotated[
        typing.Optional[EcommOrderChangedPayloadPayloadPurchasedItemsItemVariantImage],
        FieldMetadata(alias="variantImage"),
        pydantic.Field(alias="variantImage"),
    ] = None
    variant_price: typing_extensions.Annotated[
        typing.Optional[EcommOrderChangedPayloadPayloadPurchasedItemsItemVariantPrice],
        FieldMetadata(alias="variantPrice"),
        pydantic.Field(alias="variantPrice", description="The price corresponding to the variant"),
    ] = None
    """
    The price corresponding to the variant
    """

    weight: typing.Optional[float] = pydantic.Field(default=None)
    """
    The physical weight of the variant if provided, or null
    """

    width: typing.Optional[float] = pydantic.Field(default=None)
    """
    The physical width of the variant if provided, or null
    """

    height: typing.Optional[float] = pydantic.Field(default=None)
    """
    The physical height of the variant if provided, or null
    """

    length: typing.Optional[float] = pydantic.Field(default=None)
    """
    The physical length of the variant if provided, or null
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
