

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .team_member import TeamMember


class CreateTeamMemberRequest(UniversalBaseModel):
    """
    Represents a create request for a `TeamMember` object.
    """

    idempotency_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique string that identifies this `CreateTeamMember` request.
    Keys can be any valid string, but must be unique for every request.
    For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency).
    
    The minimum length is 1 and the maximum length is 45.
    """

    team_member: typing.Optional[TeamMember] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
