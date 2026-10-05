

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .quay_robot_desired_state import QuayRobotDesiredState
from .secret import Secret


class QuayOrgDesiredState(UniversalBaseModel):
    """
    Desired robot-account state for a single Quay organization.
    """

    instance_name: str = pydantic.Field()
    """
    Quay instance name
    """

    instance_url: str = pydantic.Field()
    """
    Quay instance URL or hostname
    """

    managed_repos: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether repository permissions may be reconciled
    """

    managed_robot_accounts: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Opt-in flag required to manage robot accounts in this org
    """

    managed_teams: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Teams this integration is allowed to manage
    """

    org_name: str = pydantic.Field()
    """
    Quay organization name
    """

    robots: typing.Optional[typing.List[QuayRobotDesiredState]] = pydantic.Field(default=None)
    """
    Desired robot accounts for this organization
    """

    token: Secret = pydantic.Field()
    """
    Vault secret reference for the org automation token
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
