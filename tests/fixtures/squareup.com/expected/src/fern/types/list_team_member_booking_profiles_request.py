

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListTeamMemberBookingProfilesRequest(UniversalBaseModel):
    """ """

    bookable_only: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether to include only bookable team members in the returned result (`true`) or not (`false`).
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The cursor for paginating through the results.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of results to return.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates whether to include only team members enabled at the given location in the returned result.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
