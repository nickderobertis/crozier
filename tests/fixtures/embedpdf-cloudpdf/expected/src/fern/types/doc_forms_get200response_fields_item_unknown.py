

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
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


class DocFormsGet200ResponseFieldsItemUnknown(UniversalBaseModel):
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
