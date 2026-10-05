

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .secret import Secret


class GithubOrgDesiredState(UniversalBaseModel):
    """
    Desired owner state for a single GitHub organization.

    Attributes:
        org_name: GitHub organization name
        token: Vault secret reference for the org's GitHub API token
        base_url: GitHub API base URL (override for GitHub Enterprise)
        owners: Desired set of lowercase GitHub usernames that should be org admins
    """

    base_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    GitHub API base URL (override for GitHub Enterprise)
    """

    org_name: str = pydantic.Field()
    """
    GitHub organization name
    """

    owners: typing.List[str] = pydantic.Field()
    """
    Desired set of GitHub usernames that should be org admins
    """

    token: Secret = pydantic.Field()
    """
    Vault secret reference for the GitHub API token
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
