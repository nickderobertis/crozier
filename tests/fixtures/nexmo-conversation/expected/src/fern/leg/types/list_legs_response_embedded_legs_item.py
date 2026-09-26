

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.channel_type import ChannelType
from ...types.conversation_id import ConversationId
from ...types.leg_id import LegId
from ...types.leg_state import LegState
from ...types.timestamp_leg_end_time import TimestampLegEndTime
from ...types.timestamp_leg_start_time import TimestampLegStartTime


class ListLegsResponseEmbeddedLegsItem(UniversalBaseModel):
    embedded: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="_embedded"),
        pydantic.Field(alias="_embedded"),
    ] = None
    links: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")
    ] = None
    conversation_uuid: typing.Optional[ConversationId] = None
    from_: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]], FieldMetadata(alias="from"), pydantic.Field(alias="from")
    ] = None
    start_end: typing.Optional[TimestampLegEndTime] = None
    start_time: typing.Optional[TimestampLegStartTime] = None
    state: typing.Optional[LegState] = None
    to: typing.Optional[typing.Dict[str, typing.Any]] = None
    type: typing.Optional[ChannelType] = None
    uuid_: typing_extensions.Annotated[LegId, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
