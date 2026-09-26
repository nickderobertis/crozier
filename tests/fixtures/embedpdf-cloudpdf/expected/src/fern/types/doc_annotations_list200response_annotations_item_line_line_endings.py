

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_line_line_endings_end import (
    DocAnnotationsList200ResponseAnnotationsItemLineLineEndingsEnd,
)
from .doc_annotations_list200response_annotations_item_line_line_endings_start import (
    DocAnnotationsList200ResponseAnnotationsItemLineLineEndingsStart,
)


class DocAnnotationsList200ResponseAnnotationsItemLineLineEndings(UniversalBaseModel):
    start: DocAnnotationsList200ResponseAnnotationsItemLineLineEndingsStart
    end: DocAnnotationsList200ResponseAnnotationsItemLineLineEndingsEnd

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
