

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_all_records_metadata_response_record_types_contract import ListAllRecordsMetadataResponseRecordTypesContract


class ListAllRecordsMetadataResponseRecordTypes(UniversalBaseModel):
    contract: typing.Optional[ListAllRecordsMetadataResponseRecordTypesContract] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
