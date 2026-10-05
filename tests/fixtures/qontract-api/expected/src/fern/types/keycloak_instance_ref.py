

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .secret import Secret


class KeycloakInstanceRef(UniversalBaseModel):
    """
    A Keycloak realm a managed SSO client registers against.
    """

    initial_access_token: Secret = pydantic.Field()
    """
    Vault reference to this realm's initial access token (IAT)
    """

    url: str = pydantic.Field()
    """
    Full realm base URL, e.g. https://host/auth/realms/name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
