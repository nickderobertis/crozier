

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CimdMetadata(UniversalBaseModel):
    client_id_url: str = pydantic.Field()
    """
    The HTTPS URL used as the OAuth2 client_id
    """

    redirect_uri: str = pydantic.Field()
    """
    Redirect URI from the authorization request, validated against the CIMD document
    """

    verified_domain: str = pydantic.Field()
    """
    Hostname extracted from the client_id URL
    """

    requested_scopes: typing.List[str] = pydantic.Field()
    """
    OAuth2 scopes requested in the authorization request
    """

    logo_uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    Logo URL from the CIMD document, if present. Always an absolute HTTPS URL.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
