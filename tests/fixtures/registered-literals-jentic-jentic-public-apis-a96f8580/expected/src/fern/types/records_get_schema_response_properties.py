

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .records_get_schema_response_properties_additional_notes import RecordsGetSchemaResponsePropertiesAdditionalNotes
from .records_get_schema_response_properties_agreement_date import RecordsGetSchemaResponsePropertiesAgreementDate
from .records_get_schema_response_properties_workflow_id import RecordsGetSchemaResponsePropertiesWorkflowId


class RecordsGetSchemaResponseProperties(UniversalBaseModel):
    additional_notes: typing_extensions.Annotated[
        typing.Optional[RecordsGetSchemaResponsePropertiesAdditionalNotes],
        FieldMetadata(alias="additionalNotes"),
        pydantic.Field(alias="additionalNotes"),
    ] = None
    agreement_date: typing_extensions.Annotated[
        typing.Optional[RecordsGetSchemaResponsePropertiesAgreementDate],
        FieldMetadata(alias="agreementDate"),
        pydantic.Field(alias="agreementDate"),
    ] = None
    workflow_id: typing_extensions.Annotated[
        typing.Optional[RecordsGetSchemaResponsePropertiesWorkflowId],
        FieldMetadata(alias="workflowId"),
        pydantic.Field(alias="workflowId"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
