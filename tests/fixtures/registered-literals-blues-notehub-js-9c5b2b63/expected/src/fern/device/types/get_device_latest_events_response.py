

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event import Event


class GetDeviceLatestEventsResponse(UniversalBaseModel):
    latest_events: typing.Optional[typing.List[Event]] = pydantic.Field(default=None)
    """
    The set of latest events.  Will always include the current "session.begin" event.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
