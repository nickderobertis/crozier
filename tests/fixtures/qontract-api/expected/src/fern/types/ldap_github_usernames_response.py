

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ldap_github_user import LdapGithubUser


class LdapGithubUsernamesResponse(UniversalBaseModel):
    """
    Response with resolved GitHub-username -> uid mappings.

    Only contains entries for requested logins that were found in LDAP;
    unresolved logins are omitted.
    """

    users: typing.List[LdapGithubUser] = pydantic.Field()
    """
    Resolved GitHub username to org_username mappings
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
