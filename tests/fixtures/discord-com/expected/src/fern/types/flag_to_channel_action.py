

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .flag_to_channel_action_metadata import FlagToChannelActionMetadata


class FlagToChannelAction(UniversalBaseModel):
    type: int
    metadata: FlagToChannelActionMetadata

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
