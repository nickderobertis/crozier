

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_forms_get200response_fields_item_signature_widgets_item_ref_nm_page import (
    DocFormsGet200ResponseFieldsItemSignatureWidgetsItemRefNmPage,
)


class DocFormsGet200ResponseFieldsItemSignatureWidgetsItemRefNm(UniversalBaseModel):
    page: DocFormsGet200ResponseFieldsItemSignatureWidgetsItemRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
