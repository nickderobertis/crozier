

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .authority_authorisation_domain import AuthorityAuthorisationDomain
from .pagination_properties import PaginationProperties


class AuthorityAuthorisationDomainsPage(PaginationProperties):
    content: typing.Optional[typing.List[AuthorityAuthorisationDomain]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
