

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sessions_get_response_data_sessions_item import SessionsGetResponseDataSessionsItem


class SessionsGetResponseData(UniversalBaseModel):
    sessions: typing.List[SessionsGetResponseDataSessionsItem] = pydantic.Field()
    """
    List of session summaries
    """

    total: float = pydantic.Field()
    """
    Total number of sessions matching the filter
    """

    limit: float = pydantic.Field()
    """
    Max results per page
    """

    offset: float = pydantic.Field()
    """
    Pagination offset
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
