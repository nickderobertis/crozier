

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .quay_org_key import QuayOrgKey
from .quay_repo_config import QuayRepoConfig
from .secret import Secret


class QuayOrgConfig(UniversalBaseModel):
    """
    Configuration for a single Quay organization to reconcile.
    """

    automation_token: Secret = pydantic.Field()
    """
    Secret reference for API token
    """

    base_url: str = pydantic.Field()
    """
    Quay instance base URL
    """

    instance: str = pydantic.Field()
    """
    Quay instance name
    """

    managed_repos: bool = pydantic.Field()
    """
    Whether repos are managed by app-interface
    """

    mirror: typing.Optional[QuayOrgKey] = pydantic.Field(default=None)
    """
    Upstream org this org mirrors (if any)
    """

    org_name: str = pydantic.Field()
    """
    Quay organization name
    """

    repos: typing.Optional[typing.List[QuayRepoConfig]] = pydantic.Field(default=None)
    """
    Desired repository state for this org
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
