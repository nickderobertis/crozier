

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .authorisation_domain import AuthorisationDomain
from .pagination_properties import PaginationProperties


class AuthorisationDomainsPage(PaginationProperties):
    content: typing.Optional[typing.List[AuthorisationDomain]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
