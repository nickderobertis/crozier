

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_line_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemLineRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_line_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemLineRefIndexRevision,
)


class DocAnnotationsList200ResponseAnnotationsItemLineRefIndex(UniversalBaseModel):
    page: DocAnnotationsList200ResponseAnnotationsItemLineRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemLineRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
