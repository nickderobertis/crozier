

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_forms_get200response_fields_item_checkbox_widgets_item_ref_index_page import (
    DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRefIndexPage,
)
from .doc_forms_get200response_fields_item_checkbox_widgets_item_ref_index_revision import (
    DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRefIndexRevision,
)


class DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRefIndex(UniversalBaseModel):
    page: DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRefIndexPage
    index: int
    revision: DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
