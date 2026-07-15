

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .airbyte_stream_and_configuration import AirbyteStreamAndConfiguration


class AirbyteCatalog(UniversalBaseModel):
    """
    describes the available schema (catalog).
    """

    streams: typing.List[AirbyteStreamAndConfiguration]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
