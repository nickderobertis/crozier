

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .activity import Activity
from .last_data_access_times import LastDataAccessTimes
from .request_id import RequestId


class ItemActivityListResponse(UniversalBaseModel):
    """
    Describes a historical log of user consent events.
    """

    activities: typing.List[Activity] = pydantic.Field()
    """
    A list of activities.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cursor used for pagination.
    """

    last_data_access_times: typing.List[LastDataAccessTimes] = pydantic.Field()
    """
    An array of objects containing timestamps for the last time each data type was accessed per application.
    """

    request_id: typing.Optional[RequestId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
