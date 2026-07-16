

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .search_team_members_filter import SearchTeamMembersFilter


class SearchTeamMembersQuery(UniversalBaseModel):
    """
    Represents the parameters in a search for `TeamMember` objects.
    """

    filter: typing.Optional[SearchTeamMembersFilter] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
