

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .team_member_wage import TeamMemberWage


class GetTeamMemberWageResponse(UniversalBaseModel):
    """
    A response to a request to get a `TeamMemberWage`. The response contains
    the requested `TeamMemberWage` objects and might contain a set of `Error` objects if
    the request resulted in errors.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    team_member_wage: typing.Optional[TeamMemberWage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
