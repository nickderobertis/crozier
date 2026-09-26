

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_square_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemSquareRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_square_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemSquareRefIndexRevision,
)


class DocAnnotationsList200ResponseAnnotationsItemSquareRefIndex(UniversalBaseModel):
    page: DocAnnotationsList200ResponseAnnotationsItemSquareRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemSquareRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
