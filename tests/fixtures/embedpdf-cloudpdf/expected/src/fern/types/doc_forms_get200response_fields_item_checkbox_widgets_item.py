

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_forms_get200response_fields_item_checkbox_widgets_item_page import (
    DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemPage,
)
from .doc_forms_get200response_fields_item_checkbox_widgets_item_ref import (
    DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRef,
)


class DocFormsGet200ResponseFieldsItemCheckboxWidgetsItem(UniversalBaseModel):
    ref: typing.Optional[DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRef] = None
    annot_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="annotObjectNumber"), pydantic.Field(alias="annotObjectNumber")
    ]
    page: typing.Optional[DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemPage] = None
    on_state: typing_extensions.Annotated[str, FieldMetadata(alias="onState"), pydantic.Field(alias="onState")]
    export_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="exportValue"), pydantic.Field(alias="exportValue")
    ]
    checked: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
