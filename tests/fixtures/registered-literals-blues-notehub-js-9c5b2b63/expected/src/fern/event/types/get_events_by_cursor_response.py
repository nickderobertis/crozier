

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event import Event


class GetEventsByCursorResponse(UniversalBaseModel):
    events: typing.List[Event]
    has_more: bool = pydantic.Field()
    """
    True if there are more events
    """

    next_cursor: str = pydantic.Field()
    """
    The cursor value of the next result, which is intended to be used as the "cursor" parameter value of the next call to this method. An empty string is returned if there are no more results after this results set.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
