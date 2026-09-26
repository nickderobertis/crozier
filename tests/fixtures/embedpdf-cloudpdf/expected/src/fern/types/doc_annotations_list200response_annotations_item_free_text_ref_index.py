

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_free_text_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_free_text_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRefIndexRevision,
)


class DocAnnotationsList200ResponseAnnotationsItemFreeTextRefIndex(UniversalBaseModel):
    page: DocAnnotationsList200ResponseAnnotationsItemFreeTextRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemFreeTextRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
