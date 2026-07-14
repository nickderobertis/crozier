

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .airbyte_stream import AirbyteStream
from .airbyte_stream_configuration import AirbyteStreamConfiguration


class AirbyteStreamAndConfiguration(UniversalBaseModel):
    """
    each stream is split in two parts; the immutable schema from source and mutable configuration for destination
    """

    config: typing.Optional[AirbyteStreamConfiguration] = None
    stream: typing.Optional[AirbyteStream] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
