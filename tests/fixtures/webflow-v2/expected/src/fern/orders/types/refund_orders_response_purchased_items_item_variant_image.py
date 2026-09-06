

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .refund_orders_response_purchased_items_item_variant_image_file import (
    RefundOrdersResponsePurchasedItemsItemVariantImageFile,
)


class RefundOrdersResponsePurchasedItemsItemVariantImage(UniversalBaseModel):
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The hosted location for the Variant's image
    """

    file: typing.Optional[RefundOrdersResponsePurchasedItemsItemVariantImageFile] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
