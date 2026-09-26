

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_signatures_complete200response_signature_widget_ref_nm_page import (
    DocSignaturesComplete200ResponseSignatureWidgetRefNmPage,
)


class DocSignaturesComplete200ResponseSignatureWidgetRefNm(UniversalBaseModel):
    page: DocSignaturesComplete200ResponseSignatureWidgetRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
