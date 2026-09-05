

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_creation_response_application_type import ClientCreationResponseApplicationType
from .organisation_id import OrganisationId


class ClientCreationResponse(UniversalBaseModel):
    application_type: typing.Optional[ClientCreationResponseApplicationType] = pydantic.Field(default=None)
    """
    OIDC application type response
    """

    authorization_signed_response_alg: typing.Optional[str] = None
    backchannel_user_code_parameter: typing.Optional[bool] = None
    client_id: typing.Optional[str] = None
    client_id_issued_at: typing.Optional[float] = None
    client_secret: typing.Optional[str] = None
    client_secret_expires_at: typing.Optional[float] = None
    grant_types: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    grant_types
    """

    id_token_signed_response_alg: typing.Optional[str] = None
    introspection_endpoint_auth_method: typing.Optional[str] = None
    jwks_uri: typing.Optional[str] = None
    organisation_id: typing.Optional[OrganisationId] = None
    organisation_name: typing.Optional[str] = None
    organisation_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    the cnpj number of the organisation
    """

    post_logout_redirect_uris: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    post_logout_redirect_uris
    """

    redirect_uris: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    redirect_uris
    """

    registration_access_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    token used to manage client post creation
    """

    registration_client_uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    management uri location to manage client post creation
    """

    request_object_signing_alg: typing.Optional[str] = None
    require_auth_time: typing.Optional[bool] = None
    require_pushed_authorization_requests: typing.Optional[bool] = None
    require_signed_request_object: typing.Optional[bool] = None
    response_types: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    response_types
    """

    revocation_endpoint_auth_method: typing.Optional[str] = None
    scope: typing.Optional[str] = None
    software_description: typing.Optional[str] = None
    software_id: typing.Optional[str] = None
    software_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Software Statement client name
    """

    software_roles: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    array of software roles
    """

    subject_type: typing.Optional[str] = None
    tls_client_certificate_bound_access_token: typing.Optional[bool] = None
    token_endpoint_auth_method: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
