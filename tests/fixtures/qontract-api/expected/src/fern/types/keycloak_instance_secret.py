

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .secret import Secret


class KeycloakInstanceSecret(UniversalBaseModel):
    """
    A Keycloak instance's issuer URL + the Vault location of its IAT secret.

    The Vault secret itself does not carry the issuer URL (see
    qontract_api.keycloak_iat), so the client must supply it explicitly
    alongside the secret reference.
    """

    secret: Secret = pydantic.Field()
    """
    Vault reference to the instance's initial-access-token secret
    """

    url: str = pydantic.Field()
    """
    Keycloak realm base URL (issuer)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
