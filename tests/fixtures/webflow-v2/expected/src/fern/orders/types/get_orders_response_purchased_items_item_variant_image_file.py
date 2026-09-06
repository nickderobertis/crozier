

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_orders_response_purchased_items_item_variant_image_file_variants_item import (
    GetOrdersResponsePurchasedItemsItemVariantImageFileVariantsItem,
)


class GetOrdersResponsePurchasedItemsItemVariantImageFile(UniversalBaseModel):
    size: typing.Optional[float] = pydantic.Field(default=None)
    """
    The image size in bytes
    """

    original_file_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="originalFileName"),
        pydantic.Field(alias="originalFileName", description="the original name of the image"),
    ] = None
    """
    the original name of the image
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="The creation timestamp of the image"),
    ] = None
    """
    The creation timestamp of the image
    """

    content_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contentType"),
        pydantic.Field(alias="contentType", description="The MIME type of the image"),
    ] = None
    """
    The MIME type of the image
    """

    width: typing.Optional[int] = pydantic.Field(default=None)
    """
    The image width in pixels
    """

    height: typing.Optional[int] = pydantic.Field(default=None)
    """
    The image height in pixels
    """

    variants: typing.Optional[typing.List[GetOrdersResponsePurchasedItemsItemVariantImageFileVariantsItem]] = (
        pydantic.Field(default=None)
    )
    """
    Variants of the supplied image
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
