

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_line_caption_offset import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineCaptionOffset,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_caption_position import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineCaptionPosition,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineCaption(UniversalBaseModel):
    enabled: bool
    position: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineCaptionPosition] = None
    offset: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineCaptionOffset] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
