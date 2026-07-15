

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class IssuesFilter(UniversalBaseModel):
    assignee_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Only return tickets assigned to a specific user
    """

    since: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Only return tickets since a specific date
    """

    status: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Filter by ticket status, can be `open`, `closed` or `all`. Will passthrough if none of the above match
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
