

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_all_records_metadata_response_properties_additional_notes import (
    ListAllRecordsMetadataResponsePropertiesAdditionalNotes,
)
from .list_all_records_metadata_response_properties_agreement_date import (
    ListAllRecordsMetadataResponsePropertiesAgreementDate,
)
from .list_all_records_metadata_response_properties_workflow_id import (
    ListAllRecordsMetadataResponsePropertiesWorkflowId,
)


class ListAllRecordsMetadataResponseProperties(UniversalBaseModel):
    additional_notes: typing_extensions.Annotated[
        typing.Optional[ListAllRecordsMetadataResponsePropertiesAdditionalNotes],
        FieldMetadata(alias="additionalNotes"),
        pydantic.Field(alias="additionalNotes"),
    ] = None
    agreement_date: typing_extensions.Annotated[
        typing.Optional[ListAllRecordsMetadataResponsePropertiesAgreementDate],
        FieldMetadata(alias="agreementDate"),
        pydantic.Field(alias="agreementDate"),
    ] = None
    workflow_id: typing_extensions.Annotated[
        typing.Optional[ListAllRecordsMetadataResponsePropertiesWorkflowId],
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
