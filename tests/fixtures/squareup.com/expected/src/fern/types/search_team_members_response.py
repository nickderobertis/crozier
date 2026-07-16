

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .team_member import TeamMember


class SearchTeamMembersResponse(UniversalBaseModel):
    """
    Represents a response from a search request containing a filtered list of `TeamMember` objects.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The opaque cursor for fetching the next page. For more information, see
    [pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    The errors that occurred during the request.
    """

    team_members: typing.Optional[typing.List[TeamMember]] = pydantic.Field(default=None)
    """
    The filtered list of `TeamMember` objects.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
