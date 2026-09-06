

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ecomm_new_order_payload_payload_purchased_items_item_variant_image_file import (
    EcommNewOrderPayloadPayloadPurchasedItemsItemVariantImageFile,
)


class EcommNewOrderPayloadPayloadPurchasedItemsItemVariantImage(UniversalBaseModel):
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The hosted location for the Variant's image
    """

    file: typing.Optional[EcommNewOrderPayloadPayloadPurchasedItemsItemVariantImageFile] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
