

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TeamMemberAssignedLocations(UniversalBaseModel):
    """
    An object that represents a team member's assignment to locations.
    """

    assignment_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The current assignment type of the team member.
    """

    location_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The locations that the team member is assigned to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
