

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_forms_get200response_fields_item_combobox_widgets_item_page import (
    DocFormsGet200ResponseFieldsItemComboboxWidgetsItemPage,
)
from .doc_forms_get200response_fields_item_combobox_widgets_item_ref import (
    DocFormsGet200ResponseFieldsItemComboboxWidgetsItemRef,
)


class DocFormsGet200ResponseFieldsItemComboboxWidgetsItem(UniversalBaseModel):
    ref: typing.Optional[DocFormsGet200ResponseFieldsItemComboboxWidgetsItemRef] = None
    annot_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="annotObjectNumber"), pydantic.Field(alias="annotObjectNumber")
    ]
    page: typing.Optional[DocFormsGet200ResponseFieldsItemComboboxWidgetsItemPage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
