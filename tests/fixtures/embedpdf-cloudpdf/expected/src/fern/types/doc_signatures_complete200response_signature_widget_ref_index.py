

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_signatures_complete200response_signature_widget_ref_index_page import (
    DocSignaturesComplete200ResponseSignatureWidgetRefIndexPage,
)
from .doc_signatures_complete200response_signature_widget_ref_index_revision import (
    DocSignaturesComplete200ResponseSignatureWidgetRefIndexRevision,
)


class DocSignaturesComplete200ResponseSignatureWidgetRefIndex(UniversalBaseModel):
    page: DocSignaturesComplete200ResponseSignatureWidgetRefIndexPage
    index: int
    revision: DocSignaturesComplete200ResponseSignatureWidgetRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
