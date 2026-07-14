

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_response import EventResponse


class EventsList(UniversalBaseModel):
    """
    Response envelope for paginated listing of events
    """

    item_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of events in this page
    """

    next_page: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Boolean flag, True indicates there are more events and False otherwise
    """

    page: typing.Optional[int] = pydantic.Field(default=None)
    """
    Page number of this result set
    """

    results: typing.Optional[typing.List[EventResponse]] = pydantic.Field(default=None)
    """
    List of events
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
