

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_forms_get200response_fields_item_checkbox_default_value_entry import (
    DocFormsGet200ResponseFieldsItemCheckboxDefaultValueEntry,
)
from .doc_forms_get200response_fields_item_checkbox_flags import DocFormsGet200ResponseFieldsItemCheckboxFlags
from .doc_forms_get200response_fields_item_checkbox_origin import DocFormsGet200ResponseFieldsItemCheckboxOrigin
from .doc_forms_get200response_fields_item_checkbox_ref import DocFormsGet200ResponseFieldsItemCheckboxRef
from .doc_forms_get200response_fields_item_checkbox_value_entry import (
    DocFormsGet200ResponseFieldsItemCheckboxValueEntry,
)
from .doc_forms_get200response_fields_item_checkbox_widgets_item import (
    DocFormsGet200ResponseFieldsItemCheckboxWidgetsItem,
)
from .pdf_field_actions import PdfFieldActions


class DocFormsGet200ResponseFieldsItemCheckbox(UniversalBaseModel):
    ref: DocFormsGet200ResponseFieldsItemCheckboxRef
    field_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="fieldObjectNumber"), pydantic.Field(alias="fieldObjectNumber")
    ]
    name: str
    origin: DocFormsGet200ResponseFieldsItemCheckboxOrigin
    flags: DocFormsGet200ResponseFieldsItemCheckboxFlags
    alternate_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="alternateName"), pydantic.Field(alias="alternateName")
    ] = None
    mapping_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mappingName"), pydantic.Field(alias="mappingName")
    ] = None
    value_entry: typing_extensions.Annotated[
        DocFormsGet200ResponseFieldsItemCheckboxValueEntry,
        FieldMetadata(alias="valueEntry"),
        pydantic.Field(alias="valueEntry"),
    ]
    default_value_entry: typing_extensions.Annotated[
        DocFormsGet200ResponseFieldsItemCheckboxDefaultValueEntry,
        FieldMetadata(alias="defaultValueEntry"),
        pydantic.Field(alias="defaultValueEntry"),
    ]
    actions: typing.Optional[PdfFieldActions] = None
    widgets: typing.List[DocFormsGet200ResponseFieldsItemCheckboxWidgetsItem]
    checked: bool
    export_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="exportValue"), pydantic.Field(alias="exportValue")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
