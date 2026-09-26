

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_signatures_list200response_signatures_item_widget_ref_index_page import (
    DocSignaturesList200ResponseSignaturesItemWidgetRefIndexPage,
)
from .doc_signatures_list200response_signatures_item_widget_ref_index_revision import (
    DocSignaturesList200ResponseSignaturesItemWidgetRefIndexRevision,
)


class DocSignaturesList200ResponseSignaturesItemWidgetRefIndex(UniversalBaseModel):
    page: DocSignaturesList200ResponseSignaturesItemWidgetRefIndexPage
    index: int
    revision: DocSignaturesList200ResponseSignaturesItemWidgetRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
