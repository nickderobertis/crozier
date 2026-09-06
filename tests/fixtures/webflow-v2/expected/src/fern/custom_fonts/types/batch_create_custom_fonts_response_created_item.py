

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .batch_create_custom_fonts_response_created_item_custom_font import (
    BatchCreateCustomFontsResponseCreatedItemCustomFont,
)
from .batch_create_custom_fonts_response_created_item_upload import BatchCreateCustomFontsResponseCreatedItemUpload


class BatchCreateCustomFontsResponseCreatedItem(UniversalBaseModel):
    custom_font: typing_extensions.Annotated[
        BatchCreateCustomFontsResponseCreatedItemCustomFont,
        FieldMetadata(alias="customFont"),
        pydantic.Field(alias="customFont", description="A custom font uploaded to a Webflow site"),
    ]
    """
    A custom font uploaded to a Webflow site
    """

    upload: BatchCreateCustomFontsResponseCreatedItemUpload = pydantic.Field()
    """
    Presigned S3 upload details. Post the font binary to `url` as `multipart/form-data`, including every key from `fields` plus the binary itself in a field named `file`. The `file` field must be the last field in the form.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
