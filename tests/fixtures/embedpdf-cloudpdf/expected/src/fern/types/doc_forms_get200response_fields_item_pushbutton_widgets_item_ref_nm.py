

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_forms_get200response_fields_item_pushbutton_widgets_item_ref_nm_page import (
    DocFormsGet200ResponseFieldsItemPushbuttonWidgetsItemRefNmPage,
)


class DocFormsGet200ResponseFieldsItemPushbuttonWidgetsItemRefNm(UniversalBaseModel):
    page: DocFormsGet200ResponseFieldsItemPushbuttonWidgetsItemRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
