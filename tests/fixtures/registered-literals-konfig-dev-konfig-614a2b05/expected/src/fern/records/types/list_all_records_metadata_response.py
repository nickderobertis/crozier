

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_all_records_metadata_response_attachments import ListAllRecordsMetadataResponseAttachments
from .list_all_records_metadata_response_links import ListAllRecordsMetadataResponseLinks
from .list_all_records_metadata_response_properties import ListAllRecordsMetadataResponseProperties
from .list_all_records_metadata_response_record_types import ListAllRecordsMetadataResponseRecordTypes


class ListAllRecordsMetadataResponse(UniversalBaseModel):
    record_types: typing_extensions.Annotated[
        typing.Optional[ListAllRecordsMetadataResponseRecordTypes],
        FieldMetadata(alias="recordTypes"),
        pydantic.Field(alias="recordTypes"),
    ] = None
    properties: typing.Optional[ListAllRecordsMetadataResponseProperties] = None
    attachments: typing.Optional[ListAllRecordsMetadataResponseAttachments] = None
    links: typing.Optional[ListAllRecordsMetadataResponseLinks] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
