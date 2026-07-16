

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class TeamMemberWage(UniversalBaseModel):
    """
    The hourly wage rate that a team member earns on a `Shift` for doing the job
    specified by the `title` property of this object.
    """

    hourly_rate: typing.Optional[Money] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The UUID for this object.
    """

    team_member_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `TeamMember` that this wage is assigned to.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The job title that this wage relates to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
