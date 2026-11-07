

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StorageChannelStatistic(UniversalBaseModel):
    channel_id: typing_extensions.Annotated[int, FieldMetadata(alias="channelId"), pydantic.Field(alias="channelId")]
    name: str
    selected: bool
    health: str
    last_checked_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastCheckedAt"), pydantic.Field(alias="lastCheckedAt")
    ] = None
    part_count: typing_extensions.Annotated[int, FieldMetadata(alias="partCount"), pydantic.Field(alias="partCount")]
    stored_bytes: typing_extensions.Annotated[
        int, FieldMetadata(alias="storedBytes"), pydantic.Field(alias="storedBytes")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
