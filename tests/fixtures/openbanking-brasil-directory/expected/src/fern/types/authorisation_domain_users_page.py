

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .authorisation_domain_user import AuthorisationDomainUser
from .pagination_properties import PaginationProperties


class AuthorisationDomainUsersPage(PaginationProperties):
    content: typing.Optional[typing.List[AuthorisationDomainUser]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
