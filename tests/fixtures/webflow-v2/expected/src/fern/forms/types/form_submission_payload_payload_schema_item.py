

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .form_submission_payload_payload_schema_item_field_type import FormSubmissionPayloadPayloadSchemaItemFieldType


class FormSubmissionPayloadPayloadSchemaItem(UniversalBaseModel):
    field_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fieldName"),
        pydantic.Field(alias="fieldName", description="Form field name"),
    ] = None
    """
    Form field name
    """

    field_type: typing_extensions.Annotated[
        typing.Optional[FormSubmissionPayloadPayloadSchemaItemFieldType],
        FieldMetadata(alias="fieldType"),
        pydantic.Field(alias="fieldType", description="Form field type"),
    ] = None
    """
    Form field type
    """

    field_element_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fieldElementId"),
        pydantic.Field(alias="fieldElementId", description="Element ID of the Form Field"),
    ] = None
    """
    Element ID of the Form Field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
