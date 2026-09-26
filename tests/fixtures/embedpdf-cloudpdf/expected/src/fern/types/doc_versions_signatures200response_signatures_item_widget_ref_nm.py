

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_versions_signatures200response_signatures_item_widget_ref_nm_page import (
    DocVersionsSignatures200ResponseSignaturesItemWidgetRefNmPage,
)


class DocVersionsSignatures200ResponseSignaturesItemWidgetRefNm(UniversalBaseModel):
    page: DocVersionsSignatures200ResponseSignaturesItemWidgetRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
