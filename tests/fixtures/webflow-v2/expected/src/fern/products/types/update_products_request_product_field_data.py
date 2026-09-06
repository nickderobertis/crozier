

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .update_products_request_product_field_data_ec_product_type import (
    UpdateProductsRequestProductFieldDataEcProductType,
)
from .update_products_request_product_field_data_sku_properties_item import (
    UpdateProductsRequestProductFieldDataSkuPropertiesItem,
)
from .update_products_request_product_field_data_tax_category import UpdateProductsRequestProductFieldDataTaxCategory


class UpdateProductsRequestProductFieldData(UniversalBaseModel):
    """
    Contains content-specific details for a product, covering both standard (e.g., title, description) and custom fields tailored to the product setup.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the Product
    """

    slug: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL structure of the Product in your site.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of your product
    """

    shippable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Boolean determining if the Product is shippable
    """

    sku_properties: typing_extensions.Annotated[
        typing.Optional[typing.List[UpdateProductsRequestProductFieldDataSkuPropertiesItem]],
        FieldMetadata(alias="sku-properties"),
        pydantic.Field(alias="sku-properties", description="Variant types to include in SKUs"),
    ] = None
    """
    Variant types to include in SKUs
    """

    category: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The category your product belongs to.
    """

    tax_category: typing_extensions.Annotated[
        typing.Optional[UpdateProductsRequestProductFieldDataTaxCategory],
        FieldMetadata(alias="tax-category"),
        pydantic.Field(alias="tax-category", description="Product tax class"),
    ] = None
    """
    Product tax class
    """

    default_sku: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="default-sku"),
        pydantic.Field(alias="default-sku", description="The default SKU associated with this product."),
    ] = None
    """
    The default SKU associated with this product.
    """

    ec_product_type: typing_extensions.Annotated[
        typing.Optional[UpdateProductsRequestProductFieldDataEcProductType],
        FieldMetadata(alias="ec-product-type"),
        pydantic.Field(
            alias="ec-product-type",
            description='<a href="https://university.webflow.com/lesson/add-and-manage-products-and-categories?topics=ecommerce#how-to-understand-product-types">Product types.</a> Enums reflect the following values in order: Physical, Digital, Service, Advanced"',
        ),
    ] = None
    """
    <a href="https://university.webflow.com/lesson/add-and-manage-products-and-categories?topics=ecommerce#how-to-understand-product-types">Product types.</a> Enums reflect the following values in order: Physical, Digital, Service, Advanced"
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
