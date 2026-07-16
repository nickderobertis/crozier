

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .team_member import TeamMember


class CreateTeamMemberResponse(UniversalBaseModel):
    """
    Represents a response from a create request containing the created `TeamMember` object or error messages.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    The errors that occurred during the request.
    """

    team_member: typing.Optional[TeamMember] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
