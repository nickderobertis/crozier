

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_forms_get200response_fields_item_text_widgets_item_ref_index_page import (
    DocFormsGet200ResponseFieldsItemTextWidgetsItemRefIndexPage,
)
from .doc_forms_get200response_fields_item_text_widgets_item_ref_index_revision import (
    DocFormsGet200ResponseFieldsItemTextWidgetsItemRefIndexRevision,
)


class DocFormsGet200ResponseFieldsItemTextWidgetsItemRefIndex(UniversalBaseModel):
    page: DocFormsGet200ResponseFieldsItemTextWidgetsItemRefIndexPage
    index: int
    revision: DocFormsGet200ResponseFieldsItemTextWidgetsItemRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
