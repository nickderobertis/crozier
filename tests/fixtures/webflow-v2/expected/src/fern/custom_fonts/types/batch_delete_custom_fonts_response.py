

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .batch_delete_custom_fonts_response_deleted_item import BatchDeleteCustomFontsResponseDeletedItem
from .batch_delete_custom_fonts_response_failed_item import BatchDeleteCustomFontsResponseFailedItem


class BatchDeleteCustomFontsResponse(UniversalBaseModel):
    """
    Per-item result of a bulk-delete operation
    """

    deleted: typing.List[BatchDeleteCustomFontsResponseDeletedItem]
    failed: typing.List[BatchDeleteCustomFontsResponseFailedItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
