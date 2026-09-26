

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
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
from .pdf_field_actions import PdfFieldActions


class DocFormsGet200ResponseFieldsItemListbox(UniversalBaseModel):
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
