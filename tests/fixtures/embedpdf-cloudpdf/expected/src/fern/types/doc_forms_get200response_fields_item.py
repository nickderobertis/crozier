

from __future__ import annotations

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
from .doc_forms_get200response_fields_item_combobox_default_value_entry import (
    DocFormsGet200ResponseFieldsItemComboboxDefaultValueEntry,
)
from .doc_forms_get200response_fields_item_combobox_flags import DocFormsGet200ResponseFieldsItemComboboxFlags
from .doc_forms_get200response_fields_item_combobox_options_item import (
    DocFormsGet200ResponseFieldsItemComboboxOptionsItem,
)
from .doc_forms_get200response_fields_item_combobox_origin import DocFormsGet200ResponseFieldsItemComboboxOrigin
from .doc_forms_get200response_fields_item_combobox_ref import DocFormsGet200ResponseFieldsItemComboboxRef
from .doc_forms_get200response_fields_item_combobox_value_entry import (
    DocFormsGet200ResponseFieldsItemComboboxValueEntry,
)
from .doc_forms_get200response_fields_item_combobox_widgets_item import (
    DocFormsGet200ResponseFieldsItemComboboxWidgetsItem,
)
from .doc_forms_get200response_fields_item_listbox_default_value_entry import (
    DocFormsGet200ResponseFieldsItemListboxDefaultValueEntry,
)
from .doc_forms_get200response_fields_item_listbox_flags import DocFormsGet200ResponseFieldsItemListboxFlags
from .doc_forms_get200response_fields_item_listbox_options_item import (
    DocFormsGet200ResponseFieldsItemListboxOptionsItem,
)
from .doc_forms_get200response_fields_item_listbox_origin import DocFormsGet200ResponseFieldsItemListboxOrigin
from .doc_forms_get200response_fields_item_listbox_ref import DocFormsGet200ResponseFieldsItemListboxRef
from .doc_forms_get200response_fields_item_listbox_value_entry import DocFormsGet200ResponseFieldsItemListboxValueEntry
from .doc_forms_get200response_fields_item_listbox_widgets_item import (
    DocFormsGet200ResponseFieldsItemListboxWidgetsItem,
)
from .doc_forms_get200response_fields_item_pushbutton_default_value_entry import (
    DocFormsGet200ResponseFieldsItemPushbuttonDefaultValueEntry,
)
from .doc_forms_get200response_fields_item_pushbutton_flags import DocFormsGet200ResponseFieldsItemPushbuttonFlags
from .doc_forms_get200response_fields_item_pushbutton_origin import DocFormsGet200ResponseFieldsItemPushbuttonOrigin
from .doc_forms_get200response_fields_item_pushbutton_ref import DocFormsGet200ResponseFieldsItemPushbuttonRef
from .doc_forms_get200response_fields_item_pushbutton_value_entry import (
    DocFormsGet200ResponseFieldsItemPushbuttonValueEntry,
)
from .doc_forms_get200response_fields_item_pushbutton_widgets_item import (
    DocFormsGet200ResponseFieldsItemPushbuttonWidgetsItem,
)
from .doc_forms_get200response_fields_item_radio_default_value_entry import (
    DocFormsGet200ResponseFieldsItemRadioDefaultValueEntry,
)
from .doc_forms_get200response_fields_item_radio_flags import DocFormsGet200ResponseFieldsItemRadioFlags
from .doc_forms_get200response_fields_item_radio_origin import DocFormsGet200ResponseFieldsItemRadioOrigin
from .doc_forms_get200response_fields_item_radio_ref import DocFormsGet200ResponseFieldsItemRadioRef
from .doc_forms_get200response_fields_item_radio_value_entry import DocFormsGet200ResponseFieldsItemRadioValueEntry
from .doc_forms_get200response_fields_item_radio_widgets_item import DocFormsGet200ResponseFieldsItemRadioWidgetsItem
from .doc_forms_get200response_fields_item_signature_default_value_entry import (
    DocFormsGet200ResponseFieldsItemSignatureDefaultValueEntry,
)
from .doc_forms_get200response_fields_item_signature_flags import DocFormsGet200ResponseFieldsItemSignatureFlags
from .doc_forms_get200response_fields_item_signature_origin import DocFormsGet200ResponseFieldsItemSignatureOrigin
from .doc_forms_get200response_fields_item_signature_ref import DocFormsGet200ResponseFieldsItemSignatureRef
from .doc_forms_get200response_fields_item_signature_value_entry import (
    DocFormsGet200ResponseFieldsItemSignatureValueEntry,
)
from .doc_forms_get200response_fields_item_signature_widgets_item import (
    DocFormsGet200ResponseFieldsItemSignatureWidgetsItem,
)
from .doc_forms_get200response_fields_item_text_default_value_entry import (
    DocFormsGet200ResponseFieldsItemTextDefaultValueEntry,
)
from .doc_forms_get200response_fields_item_text_flags import DocFormsGet200ResponseFieldsItemTextFlags
from .doc_forms_get200response_fields_item_text_origin import DocFormsGet200ResponseFieldsItemTextOrigin
from .doc_forms_get200response_fields_item_text_ref import DocFormsGet200ResponseFieldsItemTextRef
from .doc_forms_get200response_fields_item_text_value_entry import DocFormsGet200ResponseFieldsItemTextValueEntry
from .doc_forms_get200response_fields_item_text_widgets_item import DocFormsGet200ResponseFieldsItemTextWidgetsItem
from .doc_forms_get200response_fields_item_unknown_default_value_entry import (
    DocFormsGet200ResponseFieldsItemUnknownDefaultValueEntry,
)
from .doc_forms_get200response_fields_item_unknown_flags import DocFormsGet200ResponseFieldsItemUnknownFlags
from .doc_forms_get200response_fields_item_unknown_origin import DocFormsGet200ResponseFieldsItemUnknownOrigin
from .doc_forms_get200response_fields_item_unknown_ref import DocFormsGet200ResponseFieldsItemUnknownRef
from .doc_forms_get200response_fields_item_unknown_value_entry import DocFormsGet200ResponseFieldsItemUnknownValueEntry
from .doc_forms_get200response_fields_item_unknown_widgets_item import (
    DocFormsGet200ResponseFieldsItemUnknownWidgetsItem,
)
from .pdf_field_actions import PdfFieldActions


class DocFormsGet200ResponseFieldsItem_Text(UniversalBaseModel):
    family: typing.Literal["text"] = "text"
    ref: DocFormsGet200ResponseFieldsItemTextRef
    field_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="fieldObjectNumber"), pydantic.Field(alias="fieldObjectNumber")
    ]
    name: str
    origin: DocFormsGet200ResponseFieldsItemTextOrigin
    flags: DocFormsGet200ResponseFieldsItemTextFlags
    alternate_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="alternateName"), pydantic.Field(alias="alternateName")
    ] = None
    mapping_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mappingName"), pydantic.Field(alias="mappingName")
    ] = None
    value_entry: typing_extensions.Annotated[
        DocFormsGet200ResponseFieldsItemTextValueEntry,
        FieldMetadata(alias="valueEntry"),
        pydantic.Field(alias="valueEntry"),
    ]
    default_value_entry: typing_extensions.Annotated[
        DocFormsGet200ResponseFieldsItemTextDefaultValueEntry,
        FieldMetadata(alias="defaultValueEntry"),
        pydantic.Field(alias="defaultValueEntry"),
    ]
    actions: typing.Optional[PdfFieldActions] = None
    widgets: typing.List[DocFormsGet200ResponseFieldsItemTextWidgetsItem]
    value: str
    default_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="defaultValue"), pydantic.Field(alias="defaultValue")
    ]
    max_length: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxLength"), pydantic.Field(alias="maxLength")
    ] = None
    multiline: bool
    password: bool
    comb: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItem_Checkbox(UniversalBaseModel):
    family: typing.Literal["checkbox"] = "checkbox"
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


class DocFormsGet200ResponseFieldsItem_Radio(UniversalBaseModel):
    family: typing.Literal["radio"] = "radio"
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


class DocFormsGet200ResponseFieldsItem_Combobox(UniversalBaseModel):
    family: typing.Literal["combobox"] = "combobox"
    ref: DocFormsGet200ResponseFieldsItemComboboxRef
    field_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="fieldObjectNumber"), pydantic.Field(alias="fieldObjectNumber")
    ]
    name: str
    origin: DocFormsGet200ResponseFieldsItemComboboxOrigin
    flags: DocFormsGet200ResponseFieldsItemComboboxFlags
    alternate_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="alternateName"), pydantic.Field(alias="alternateName")
    ] = None
    mapping_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mappingName"), pydantic.Field(alias="mappingName")
    ] = None
    value_entry: typing_extensions.Annotated[
        DocFormsGet200ResponseFieldsItemComboboxValueEntry,
        FieldMetadata(alias="valueEntry"),
        pydantic.Field(alias="valueEntry"),
    ]
    default_value_entry: typing_extensions.Annotated[
        DocFormsGet200ResponseFieldsItemComboboxDefaultValueEntry,
        FieldMetadata(alias="defaultValueEntry"),
        pydantic.Field(alias="defaultValueEntry"),
    ]
    actions: typing.Optional[PdfFieldActions] = None
    widgets: typing.List[DocFormsGet200ResponseFieldsItemComboboxWidgetsItem]
    value: str
    default_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="defaultValue"), pydantic.Field(alias="defaultValue")
    ]
    edit: bool
    options: typing.List[DocFormsGet200ResponseFieldsItemComboboxOptionsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItem_Listbox(UniversalBaseModel):
    family: typing.Literal["listbox"] = "listbox"
    ref: DocFormsGet200ResponseFieldsItemListboxRef
    field_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="fieldObjectNumber"), pydantic.Field(alias="fieldObjectNumber")
    ]
    name: str
    origin: DocFormsGet200ResponseFieldsItemListboxOrigin
    flags: DocFormsGet200ResponseFieldsItemListboxFlags
    alternate_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="alternateName"), pydantic.Field(alias="alternateName")
    ] = None
    mapping_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mappingName"), pydantic.Field(alias="mappingName")
    ] = None
    value_entry: typing_extensions.Annotated[
        DocFormsGet200ResponseFieldsItemListboxValueEntry,
        FieldMetadata(alias="valueEntry"),
        pydantic.Field(alias="valueEntry"),
    ]
    default_value_entry: typing_extensions.Annotated[
        DocFormsGet200ResponseFieldsItemListboxDefaultValueEntry,
        FieldMetadata(alias="defaultValueEntry"),
        pydantic.Field(alias="defaultValueEntry"),
    ]
    actions: typing.Optional[PdfFieldActions] = None
    widgets: typing.List[DocFormsGet200ResponseFieldsItemListboxWidgetsItem]
    selected_values: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="selectedValues"), pydantic.Field(alias="selectedValues")
    ]
    multi_select: typing_extensions.Annotated[
        bool, FieldMetadata(alias="multiSelect"), pydantic.Field(alias="multiSelect")
    ]
    options: typing.List[DocFormsGet200ResponseFieldsItemListboxOptionsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItem_Pushbutton(UniversalBaseModel):
    family: typing.Literal["pushbutton"] = "pushbutton"
    ref: DocFormsGet200ResponseFieldsItemPushbuttonRef
    field_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="fieldObjectNumber"), pydantic.Field(alias="fieldObjectNumber")
    ]
    name: str
    origin: DocFormsGet200ResponseFieldsItemPushbuttonOrigin
    flags: DocFormsGet200ResponseFieldsItemPushbuttonFlags
    alternate_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="alternateName"), pydantic.Field(alias="alternateName")
    ] = None
    mapping_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mappingName"), pydantic.Field(alias="mappingName")
    ] = None
    value_entry: typing_extensions.Annotated[
        DocFormsGet200ResponseFieldsItemPushbuttonValueEntry,
        FieldMetadata(alias="valueEntry"),
        pydantic.Field(alias="valueEntry"),
    ]
    default_value_entry: typing_extensions.Annotated[
        DocFormsGet200ResponseFieldsItemPushbuttonDefaultValueEntry,
        FieldMetadata(alias="defaultValueEntry"),
        pydantic.Field(alias="defaultValueEntry"),
    ]
    actions: typing.Optional[PdfFieldActions] = None
    widgets: typing.List[DocFormsGet200ResponseFieldsItemPushbuttonWidgetsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItem_Signature(UniversalBaseModel):
    family: typing.Literal["signature"] = "signature"
    ref: DocFormsGet200ResponseFieldsItemSignatureRef
    field_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="fieldObjectNumber"), pydantic.Field(alias="fieldObjectNumber")
    ]
    name: str
    origin: DocFormsGet200ResponseFieldsItemSignatureOrigin
    flags: DocFormsGet200ResponseFieldsItemSignatureFlags
    alternate_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="alternateName"), pydantic.Field(alias="alternateName")
    ] = None
    mapping_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mappingName"), pydantic.Field(alias="mappingName")
    ] = None
    value_entry: typing_extensions.Annotated[
        DocFormsGet200ResponseFieldsItemSignatureValueEntry,
        FieldMetadata(alias="valueEntry"),
        pydantic.Field(alias="valueEntry"),
    ]
    default_value_entry: typing_extensions.Annotated[
        DocFormsGet200ResponseFieldsItemSignatureDefaultValueEntry,
        FieldMetadata(alias="defaultValueEntry"),
        pydantic.Field(alias="defaultValueEntry"),
    ]
    actions: typing.Optional[PdfFieldActions] = None
    widgets: typing.List[DocFormsGet200ResponseFieldsItemSignatureWidgetsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItem_Unknown(UniversalBaseModel):
    family: typing.Literal["unknown"] = "unknown"
    ref: DocFormsGet200ResponseFieldsItemUnknownRef
    field_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="fieldObjectNumber"), pydantic.Field(alias="fieldObjectNumber")
    ]
    name: str
    origin: DocFormsGet200ResponseFieldsItemUnknownOrigin
    flags: DocFormsGet200ResponseFieldsItemUnknownFlags
    alternate_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="alternateName"), pydantic.Field(alias="alternateName")
    ] = None
    mapping_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mappingName"), pydantic.Field(alias="mappingName")
    ] = None
    value_entry: typing_extensions.Annotated[
        DocFormsGet200ResponseFieldsItemUnknownValueEntry,
        FieldMetadata(alias="valueEntry"),
        pydantic.Field(alias="valueEntry"),
    ]
    default_value_entry: typing_extensions.Annotated[
        DocFormsGet200ResponseFieldsItemUnknownDefaultValueEntry,
        FieldMetadata(alias="defaultValueEntry"),
        pydantic.Field(alias="defaultValueEntry"),
    ]
    actions: typing.Optional[PdfFieldActions] = None
    widgets: typing.List[DocFormsGet200ResponseFieldsItemUnknownWidgetsItem]
    raw_value: typing_extensions.Annotated[str, FieldMetadata(alias="rawValue"), pydantic.Field(alias="rawValue")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocFormsGet200ResponseFieldsItem = typing_extensions.Annotated[
    typing.Union[
        DocFormsGet200ResponseFieldsItem_Text,
        DocFormsGet200ResponseFieldsItem_Checkbox,
        DocFormsGet200ResponseFieldsItem_Radio,
        DocFormsGet200ResponseFieldsItem_Combobox,
        DocFormsGet200ResponseFieldsItem_Listbox,
        DocFormsGet200ResponseFieldsItem_Pushbutton,
        DocFormsGet200ResponseFieldsItem_Signature,
        DocFormsGet200ResponseFieldsItem_Unknown,
    ],
    pydantic.Field(discriminator="family"),
]
