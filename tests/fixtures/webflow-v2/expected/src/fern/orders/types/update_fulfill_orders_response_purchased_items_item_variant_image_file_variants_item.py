

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class UpdateFulfillOrdersResponsePurchasedItemsItemVariantImageFileVariantsItem(UniversalBaseModel):
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The hosted location for the Variant's image
    """

    original_file_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="originalFileName"), pydantic.Field(alias="originalFileName")
    ] = None
    size: typing.Optional[float] = pydantic.Field(default=None)
    """
    The image size in bytes
    """

    width: typing.Optional[int] = pydantic.Field(default=None)
    """
    The image width in pixels
    """

    height: typing.Optional[int] = pydantic.Field(default=None)
    """
    The image height in pixels
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
