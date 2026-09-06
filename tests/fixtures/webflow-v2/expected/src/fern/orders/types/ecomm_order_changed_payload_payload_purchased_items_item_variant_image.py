

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ecomm_order_changed_payload_payload_purchased_items_item_variant_image_file import (
    EcommOrderChangedPayloadPayloadPurchasedItemsItemVariantImageFile,
)


class EcommOrderChangedPayloadPayloadPurchasedItemsItemVariantImage(UniversalBaseModel):
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The hosted location for the Variant's image
    """

    file: typing.Optional[EcommOrderChangedPayloadPayloadPurchasedItemsItemVariantImageFile] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
