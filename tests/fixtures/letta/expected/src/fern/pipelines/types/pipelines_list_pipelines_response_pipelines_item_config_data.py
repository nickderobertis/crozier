

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipelines_list_pipelines_response_pipelines_item_config_data_channels_item import (
    PipelinesListPipelinesResponsePipelinesItemConfigDataChannelsItem,
)


class PipelinesListPipelinesResponsePipelinesItemConfigData(UniversalBaseModel):
    channels: typing.List[PipelinesListPipelinesResponsePipelinesItemConfigDataChannelsItem]
    max_messages_per_poll: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
