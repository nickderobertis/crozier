

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_forms_get200response_fields_item_radio_widgets_item_page import (
    DocFormsGet200ResponseFieldsItemRadioWidgetsItemPage,
)
from .doc_forms_get200response_fields_item_radio_widgets_item_ref import (
    DocFormsGet200ResponseFieldsItemRadioWidgetsItemRef,
)


class DocFormsGet200ResponseFieldsItemRadioWidgetsItem(UniversalBaseModel):
    ref: typing.Optional[DocFormsGet200ResponseFieldsItemRadioWidgetsItemRef] = None
    annot_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="annotObjectNumber"), pydantic.Field(alias="annotObjectNumber")
    ]
    page: typing.Optional[DocFormsGet200ResponseFieldsItemRadioWidgetsItemPage] = None
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
