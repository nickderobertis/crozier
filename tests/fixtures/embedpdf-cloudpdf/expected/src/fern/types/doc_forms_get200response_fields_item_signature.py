

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
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
from .pdf_field_actions import PdfFieldActions


class DocFormsGet200ResponseFieldsItemSignature(UniversalBaseModel):
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
