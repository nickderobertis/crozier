

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_sku_products_response_skus_item_field_data_sku_properties_item_enum_item import (
    CreateSkuProductsResponseSkusItemFieldDataSkuPropertiesItemEnumItem,
)


class CreateSkuProductsResponseSkusItemFieldDataSkuPropertiesItem(UniversalBaseModel):
    """
    A variant/option type for a SKU
    """

    id: str = pydantic.Field()
    """
    Unique identifier for a collection of Product Variants
    """

    name: str = pydantic.Field()
    """
    Name of the collection of Product Variants
    """

    enum: typing.List[CreateSkuProductsResponseSkusItemFieldDataSkuPropertiesItemEnumItem] = pydantic.Field()
    """
    The individual Product variants that are contained within the collection
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
