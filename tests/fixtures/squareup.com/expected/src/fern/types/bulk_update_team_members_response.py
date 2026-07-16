

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .update_team_member_response import UpdateTeamMemberResponse


class BulkUpdateTeamMembersResponse(UniversalBaseModel):
    """
    Represents a response from a bulk update request containing the updated `TeamMember` objects or error messages.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    The errors that occurred during the request.
    """

    team_members: typing.Optional[typing.Dict[str, UpdateTeamMemberResponse]] = pydantic.Field(default=None)
    """
    The successfully updated `TeamMember` objects. Each key is the `team_member_id` that maps to the `UpdateTeamMemberRequest`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
