

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListTeamMemberWagesRequest(UniversalBaseModel):
    """
    A request for a set of `TeamMemberWage` objects.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pointer to the next page of `EmployeeWage` results to fetch.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of `TeamMemberWage` results to return per page. The number can range between
    1 and 200. The default is 200.
    """

    team_member_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Filter the returned wages to only those that are associated with the
    specified team member.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
