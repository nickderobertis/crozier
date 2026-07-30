

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destination_config import DestinationConfig
from .pipeline_config_streams_item import PipelineConfigStreamsItem
from .source_config import SourceConfig


class PipelineConfig(UniversalBaseModel):
    source: SourceConfig
    destination: DestinationConfig
    streams: typing.Optional[typing.List[PipelineConfigStreamsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
