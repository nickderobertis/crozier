

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_streams_response_streams_item import GetStreamsResponseStreamsItem


class GetStreamsResponse(UniversalBaseModel):
    result: typing.Any
    msg: typing.Any
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    streams: typing.Optional[typing.List[GetStreamsResponseStreamsItem]] = pydantic.Field(default=None)
    """
    A list of channel objects with details on the requested channels.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
