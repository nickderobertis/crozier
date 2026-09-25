

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_events_response_events_item import GetEventsResponseEventsItem


class GetEventsResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    events: typing.Optional[typing.List[GetEventsResponseEventsItem]] = pydantic.Field(default=None)
    """
    An array of `event` objects (possibly zero-length if `dont_block` is
    set) with IDs newer than `last_event_id`. Event IDs are
    guaranteed to be increasing, but they are not guaranteed to be
    consecutive.
    """

    queue_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the registered queue.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
