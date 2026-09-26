

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_underline_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_underline_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineRefIndexRevision,
)


class DocAnnotationsList200ResponseAnnotationsItemUnderlineRefIndex(UniversalBaseModel):
    page: DocAnnotationsList200ResponseAnnotationsItemUnderlineRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemUnderlineRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
