

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_forms_get200response_fields_item_text_widgets_item_ref_object_number_page import (
    DocFormsGet200ResponseFieldsItemTextWidgetsItemRefObjectNumberPage,
)


class DocFormsGet200ResponseFieldsItemTextWidgetsItemRefObjectNumber(UniversalBaseModel):
    page: DocFormsGet200ResponseFieldsItemTextWidgetsItemRefObjectNumberPage
    annot_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="annotObjectNumber"), pydantic.Field(alias="annotObjectNumber")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
