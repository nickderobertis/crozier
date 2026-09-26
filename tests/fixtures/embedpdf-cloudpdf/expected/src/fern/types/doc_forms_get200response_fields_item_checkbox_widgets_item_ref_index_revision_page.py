

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_forms_get200response_fields_item_checkbox_widgets_item_ref_index_revision_page_kind import (
    DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRefIndexRevisionPageKind,
)


class DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRefIndexRevisionPage(UniversalBaseModel):
    kind: DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRefIndexRevisionPageKind
    page_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="pageObjectNumber"), pydantic.Field(alias="pageObjectNumber")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
