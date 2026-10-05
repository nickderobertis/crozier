

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LdapUserStatus(UniversalBaseModel):
    """
    Existence status of a single LDAP user.
    """

    exists: bool = pydantic.Field()
    """
    Whether the user exists in LDAP
    """

    username: str = pydantic.Field()
    """
    Username
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
