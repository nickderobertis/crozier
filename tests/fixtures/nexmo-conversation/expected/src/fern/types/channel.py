

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .channel_from import ChannelFrom
from .channel_leg_ids_item import ChannelLegIdsItem
from .channel_to import ChannelTo
from .channel_type import ChannelType
from .leg_id import LegId


class Channel(UniversalBaseModel):
    """
    A user who joins a conversation as a member can have one channel per membership type. Channels can be `app`, `phone`, `sip`, `websocket`, or `vbc`
    """

    from_: typing_extensions.Annotated[
        typing.Optional[ChannelFrom], FieldMetadata(alias="from"), pydantic.Field(alias="from")
    ] = None
    leg_id: typing.Optional[LegId] = None
    leg_ids: typing.Optional[typing.List[ChannelLegIdsItem]] = pydantic.Field(default=None)
    """
    Leg ids associated with this Channel. The first item in the array represents the main active Leg. The second item, if exists, represents a screen-share Leg.
    """

    to: typing.Optional[ChannelTo] = None
    type: typing.Optional[ChannelType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
