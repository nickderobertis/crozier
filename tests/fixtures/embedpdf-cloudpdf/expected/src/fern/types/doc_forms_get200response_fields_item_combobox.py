

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
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
from .pdf_field_actions import PdfFieldActions


class DocFormsGet200ResponseFieldsItemCombobox(UniversalBaseModel):
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
