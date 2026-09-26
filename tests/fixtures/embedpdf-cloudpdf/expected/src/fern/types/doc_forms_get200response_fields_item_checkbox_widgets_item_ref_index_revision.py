

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_forms_get200response_fields_item_checkbox_widgets_item_ref_index_revision_page import (
    DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRefIndexRevisionPage,
)


class DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRefIndexRevision(UniversalBaseModel):
    doc_session_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="docSessionId"), pydantic.Field(alias="docSessionId")
    ]
    page: DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRefIndexRevisionPage
    generation: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
