

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .o_auth_scope import OAuthScope


class ThirdPartyService(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique service identifier
    """

    display_name: str = pydantic.Field()
    """
    Human-readable service name
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Service description
    """

    scopes: typing.List[OAuthScope] = pydantic.Field()
    """
    Available OAuth2 scopes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
