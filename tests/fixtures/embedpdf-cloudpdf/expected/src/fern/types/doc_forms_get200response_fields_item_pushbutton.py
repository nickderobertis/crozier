

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
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
from .pdf_field_actions import PdfFieldActions


class DocFormsGet200ResponseFieldsItemPushbutton(UniversalBaseModel):
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
