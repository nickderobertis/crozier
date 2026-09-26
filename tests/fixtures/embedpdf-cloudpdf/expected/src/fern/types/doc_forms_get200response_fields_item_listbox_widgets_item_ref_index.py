

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_forms_get200response_fields_item_listbox_widgets_item_ref_index_page import (
    DocFormsGet200ResponseFieldsItemListboxWidgetsItemRefIndexPage,
)
from .doc_forms_get200response_fields_item_listbox_widgets_item_ref_index_revision import (
    DocFormsGet200ResponseFieldsItemListboxWidgetsItemRefIndexRevision,
)


class DocFormsGet200ResponseFieldsItemListboxWidgetsItemRefIndex(UniversalBaseModel):
    page: DocFormsGet200ResponseFieldsItemListboxWidgetsItemRefIndexPage
    index: int
    revision: DocFormsGet200ResponseFieldsItemListboxWidgetsItemRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
