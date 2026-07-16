

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .team_member_wage import TeamMemberWage


class ListTeamMemberWagesResponse(UniversalBaseModel):
    """
    The response to a request for a set of `TeamMemberWage` objects. The response contains
    a set of `TeamMemberWage` objects.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The value supplied in the subsequent request to fetch the next page
    of `TeamMemberWage` results.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    team_member_wages: typing.Optional[typing.List[TeamMemberWage]] = pydantic.Field(default=None)
    """
    A page of `TeamMemberWage` results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
