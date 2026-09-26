

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_signatures_list200response_signatures_item_widget_ref_nm_page import (
    DocSignaturesList200ResponseSignaturesItemWidgetRefNmPage,
)


class DocSignaturesList200ResponseSignaturesItemWidgetRefNm(UniversalBaseModel):
    page: DocSignaturesList200ResponseSignaturesItemWidgetRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
