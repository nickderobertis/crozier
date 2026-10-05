

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LdapGithubUser(UniversalBaseModel):
    """
    Resolved mapping of a single GitHub username to an LDAP uid.
    """

    github_username: str = pydantic.Field()
    """
    GitHub username (as requested)
    """

    org_username: str = pydantic.Field()
    """
    LDAP uid (app-interface org_username)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
