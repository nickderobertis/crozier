

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .job_assignment import JobAssignment


class WageSetting(UniversalBaseModel):
    """
    An object representing a team member's wage information.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp, in RFC 3339 format, describing when the wage setting object was created.
    For example, "2018-10-04T04:00:00-07:00" or "2019-02-05T12:00:00Z".
    """

    is_overtime_exempt: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the team member is exempt from the overtime rules of the seller's country.
    """

    job_assignments: typing.Optional[typing.List[JobAssignment]] = pydantic.Field(default=None)
    """
    Required. The ordered list of jobs that the team member is assigned to.
    The first job assignment is considered the team member's primary job.
    
    The minimum length is 1 and the maximum length is 12.
    """

    team_member_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of the `TeamMember` whom this wage setting describes.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp, in RFC 3339 format, describing when the wage setting object was last updated.
    For example, "2018-10-04T04:00:00-07:00" or "2019-02-05T12:00:00Z".
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Used for resolving concurrency issues. The request fails if the version
    provided does not match the server version at the time of the request. If not provided,
    Square executes a blind write, potentially overwriting data from another write. For more information,
    see [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
