

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_team_member_response import CreateTeamMemberResponse
from .error import Error


class BulkCreateTeamMembersResponse(UniversalBaseModel):
    """
    Represents a response from a bulk create request containing the created `TeamMember` objects or error messages.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    The errors that occurred during the request.
    """

    team_members: typing.Optional[typing.Dict[str, CreateTeamMemberResponse]] = pydantic.Field(default=None)
    """
    The successfully created `TeamMember` objects. Each key is the `idempotency_key` that maps to the `CreateTeamMemberRequest`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
