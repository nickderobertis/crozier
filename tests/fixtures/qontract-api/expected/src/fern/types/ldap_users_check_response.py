

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ldap_user_status import LdapUserStatus


class LdapUsersCheckResponse(UniversalBaseModel):
    """
    Response with existence status per username.
    """

    users: typing.Optional[typing.List[LdapUserStatus]] = pydantic.Field(default=None)
    """
    Existence status for each requested username
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
