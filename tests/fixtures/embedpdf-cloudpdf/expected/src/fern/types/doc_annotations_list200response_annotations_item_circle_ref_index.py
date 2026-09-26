

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_circle_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemCircleRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_circle_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemCircleRefIndexRevision,
)


class DocAnnotationsList200ResponseAnnotationsItemCircleRefIndex(UniversalBaseModel):
    page: DocAnnotationsList200ResponseAnnotationsItemCircleRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemCircleRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
