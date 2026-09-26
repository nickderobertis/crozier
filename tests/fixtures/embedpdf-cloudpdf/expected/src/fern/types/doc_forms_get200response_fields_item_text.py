

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_forms_get200response_fields_item_text_default_value_entry import (
    DocFormsGet200ResponseFieldsItemTextDefaultValueEntry,
)
from .doc_forms_get200response_fields_item_text_flags import DocFormsGet200ResponseFieldsItemTextFlags
from .doc_forms_get200response_fields_item_text_origin import DocFormsGet200ResponseFieldsItemTextOrigin
from .doc_forms_get200response_fields_item_text_ref import DocFormsGet200ResponseFieldsItemTextRef
from .doc_forms_get200response_fields_item_text_value_entry import DocFormsGet200ResponseFieldsItemTextValueEntry
from .doc_forms_get200response_fields_item_text_widgets_item import DocFormsGet200ResponseFieldsItemTextWidgetsItem
from .pdf_field_actions import PdfFieldActions


class DocFormsGet200ResponseFieldsItemText(UniversalBaseModel):
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
