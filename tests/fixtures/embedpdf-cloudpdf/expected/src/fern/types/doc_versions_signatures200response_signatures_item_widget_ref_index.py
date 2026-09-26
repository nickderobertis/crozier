

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_versions_signatures200response_signatures_item_widget_ref_index_page import (
    DocVersionsSignatures200ResponseSignaturesItemWidgetRefIndexPage,
)
from .doc_versions_signatures200response_signatures_item_widget_ref_index_revision import (
    DocVersionsSignatures200ResponseSignaturesItemWidgetRefIndexRevision,
)


class DocVersionsSignatures200ResponseSignaturesItemWidgetRefIndex(UniversalBaseModel):
    page: DocVersionsSignatures200ResponseSignaturesItemWidgetRefIndexPage
    index: int
    revision: DocVersionsSignatures200ResponseSignaturesItemWidgetRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
