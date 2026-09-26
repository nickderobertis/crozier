

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_widget_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_widget_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetRefIndexRevision,
)


class DocAnnotationsList200ResponseAnnotationsItemWidgetRefIndex(UniversalBaseModel):
    page: DocAnnotationsList200ResponseAnnotationsItemWidgetRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemWidgetRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
