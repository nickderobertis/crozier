

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRefIndexRevision,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRefIndex(UniversalBaseModel):
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
