

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .batch_create_custom_fonts_response_created_item import BatchCreateCustomFontsResponseCreatedItem
from .batch_create_custom_fonts_response_failed_item import BatchCreateCustomFontsResponseFailedItem


class BatchCreateCustomFontsResponse(UniversalBaseModel):
    """
    Per-item result of a bulk-create operation
    """

    created: typing.List[BatchCreateCustomFontsResponseCreatedItem] = pydantic.Field()
    """
    Successfully registered fonts, each with its own presigned S3 upload details.
    """

    failed: typing.List[BatchCreateCustomFontsResponseFailedItem] = pydantic.Field()
    """
    Requested fonts that could not be registered. Valid fonts elsewhere in the batch are still registered.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
