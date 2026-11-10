

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .contract_dto_type import ContractDtoType


class ContractDto(UniversalBaseModel):
    id: str
    contract_id: typing_extensions.Annotated[str, FieldMetadata(alias="contractId"), pydantic.Field(alias="contractId")]
    description: str
    owner: str
    permissions: float
    topic_id: typing_extensions.Annotated[str, FieldMetadata(alias="topicId"), pydantic.Field(alias="topicId")]
    type: ContractDtoType
    sync_requests_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="syncRequestsDate"), pydantic.Field(alias="syncRequestsDate")
    ]
    sync_pools_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="syncPoolsDate"), pydantic.Field(alias="syncPoolsDate")
    ]
    last_sync_event_time_stamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="lastSyncEventTimeStamp"), pydantic.Field(alias="lastSyncEventTimeStamp")
    ]
    wipe_contract_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="wipeContractIds"), pydantic.Field(alias="wipeContractIds")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
