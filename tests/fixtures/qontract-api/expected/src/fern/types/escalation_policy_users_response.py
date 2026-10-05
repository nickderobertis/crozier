

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pager_duty_user import PagerDutyUser


class EscalationPolicyUsersResponse(UniversalBaseModel):
    """
    Response model for escalation policy users endpoint.

    Immutable response containing list of users in an escalation policy.

    Attributes:
        users: List of users in escalation policy
    """

    users: typing.Optional[typing.List[PagerDutyUser]] = pydantic.Field(default=None)
    """
    List of users in the escalation policy
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
