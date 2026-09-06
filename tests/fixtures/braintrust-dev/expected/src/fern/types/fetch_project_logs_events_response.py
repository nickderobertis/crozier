

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_logs_event import ProjectLogsEvent


class FetchProjectLogsEventsResponse(UniversalBaseModel):
    events: typing.List[ProjectLogsEvent] = pydantic.Field()
    """
    A list of fetched events
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    Pagination cursor
    
    Pass this string directly as the `cursor` param to your next fetch request to get the next page of results. Not provided if the returned result set is empty.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
