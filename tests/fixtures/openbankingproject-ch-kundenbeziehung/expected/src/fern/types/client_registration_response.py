

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_registration_response_fapi_compliance_level import ClientRegistrationResponseFapiComplianceLevel
from .client_registration_response_swiss_standards_support import ClientRegistrationResponseSwissStandardsSupport


class ClientRegistrationResponse(UniversalBaseModel):
    client_id: str = pydantic.Field()
    """
    Unique client identifier
    """

    client_secret: typing.Optional[str] = pydantic.Field(default=None)
    """
    Client secret (if applicable)
    """

    client_secret_expires_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    Client secret expiration time (0 means no expiration)
    """

    client_id_issued_at: int = pydantic.Field()
    """
    Client ID issued time (Unix timestamp)
    """

    registration_access_token: str = pydantic.Field()
    """
    Token for accessing registration endpoint
    """

    registration_client_uri: str = pydantic.Field()
    """
    URI for client configuration management
    """

    client_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Client name
    """

    redirect_uris: typing.Optional[typing.List[str]] = None
    grant_types: typing.Optional[typing.List[str]] = None
    response_types: typing.Optional[typing.List[str]] = None
    scope: typing.Optional[str] = None
    token_endpoint_auth_method: typing.Optional[str] = None
    require_pushed_authorization_requests: typing.Optional[bool] = None
    require_signed_request_object: typing.Optional[bool] = None
    fapi_compliance_level: typing.Optional[ClientRegistrationResponseFapiComplianceLevel] = None
    industry_type: typing.Optional[str] = None
    swiss_standards_support: typing.Optional[ClientRegistrationResponseSwissStandardsSupport] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
