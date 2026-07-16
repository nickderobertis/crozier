

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AttemptStats(UniversalBaseModel):
    bytes_emitted: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="bytesEmitted"), pydantic.Field(alias="bytesEmitted")
    ] = None
    estimated_bytes: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="estimatedBytes"), pydantic.Field(alias="estimatedBytes")
    ] = None
    estimated_records: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="estimatedRecords"), pydantic.Field(alias="estimatedRecords")
    ] = None
    records_committed: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="recordsCommitted"), pydantic.Field(alias="recordsCommitted")
    ] = None
    records_emitted: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="recordsEmitted"), pydantic.Field(alias="recordsEmitted")
    ] = None
    state_messages_emitted: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="stateMessagesEmitted"), pydantic.Field(alias="stateMessagesEmitted")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
