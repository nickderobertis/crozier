

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_line_caption_offset import (
    DocAnnotationsList200ResponseAnnotationsItemLineCaptionOffset,
)
from .doc_annotations_list200response_annotations_item_line_caption_position import (
    DocAnnotationsList200ResponseAnnotationsItemLineCaptionPosition,
)


class DocAnnotationsList200ResponseAnnotationsItemLineCaption(UniversalBaseModel):
    enabled: bool
    position: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLineCaptionPosition] = None
    offset: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLineCaptionOffset] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
