

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_line_line_endings_end import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineLineEndingsEnd,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_line_endings_start import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineLineEndingsStart,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineLineEndings(UniversalBaseModel):
    start: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineLineEndingsStart
    end: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineLineEndingsEnd

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
