

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_forms_get200response_fields_item_radio_default_value_entry import (
    DocFormsGet200ResponseFieldsItemRadioDefaultValueEntry,
)
from .doc_forms_get200response_fields_item_radio_flags import DocFormsGet200ResponseFieldsItemRadioFlags
from .doc_forms_get200response_fields_item_radio_origin import DocFormsGet200ResponseFieldsItemRadioOrigin
from .doc_forms_get200response_fields_item_radio_ref import DocFormsGet200ResponseFieldsItemRadioRef
from .doc_forms_get200response_fields_item_radio_value_entry import DocFormsGet200ResponseFieldsItemRadioValueEntry
from .doc_forms_get200response_fields_item_radio_widgets_item import DocFormsGet200ResponseFieldsItemRadioWidgetsItem
from .pdf_field_actions import PdfFieldActions


class DocFormsGet200ResponseFieldsItemRadio(UniversalBaseModel):
    ref: DocFormsGet200ResponseFieldsItemRadioRef
    field_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="fieldObjectNumber"), pydantic.Field(alias="fieldObjectNumber")
    ]
    name: str
    origin: DocFormsGet200ResponseFieldsItemRadioOrigin
    flags: DocFormsGet200ResponseFieldsItemRadioFlags
    alternate_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="alternateName"), pydantic.Field(alias="alternateName")
    ] = None
    mapping_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mappingName"), pydantic.Field(alias="mappingName")
    ] = None
    value_entry: typing_extensions.Annotated[
        DocFormsGet200ResponseFieldsItemRadioValueEntry,
        FieldMetadata(alias="valueEntry"),
        pydantic.Field(alias="valueEntry"),
    ]
    default_value_entry: typing_extensions.Annotated[
        DocFormsGet200ResponseFieldsItemRadioDefaultValueEntry,
        FieldMetadata(alias="defaultValueEntry"),
        pydantic.Field(alias="defaultValueEntry"),
    ]
    actions: typing.Optional[PdfFieldActions] = None
    widgets: typing.List[DocFormsGet200ResponseFieldsItemRadioWidgetsItem]
    value: str
    radios_in_unison: typing_extensions.Annotated[
        bool, FieldMetadata(alias="radiosInUnison"), pydantic.Field(alias="radiosInUnison")
    ]
    no_toggle_to_off: typing_extensions.Annotated[
        bool, FieldMetadata(alias="noToggleToOff"), pydantic.Field(alias="noToggleToOff")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
