

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SsoClientAuth(UniversalBaseModel):
    """
    Authentication configuration for a cluster's SSO client.
    """

    group_filter_regex: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional group filter regex for the SSO client
    """

    issuer: str = pydantic.Field()
    """
    Keycloak instance URL (routes to the matching KeycloakApi)
    """

    name: str = pydantic.Field()
    """
    Auth name, must match the redirect URL
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
