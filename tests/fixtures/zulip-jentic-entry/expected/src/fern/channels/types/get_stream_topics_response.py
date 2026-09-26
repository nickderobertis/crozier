

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_stream_topics_response_topics_item import GetStreamTopicsResponseTopicsItem


class GetStreamTopicsResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    topics: typing.Optional[typing.List[GetStreamTopicsResponseTopicsItem]] = pydantic.Field(default=None)
    """
    An array of objects with information about user-accessible
    topics in the specified channel, sorted by recency (i.e.,
    the topic with the most recent message is ordered first).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
