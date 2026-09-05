

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_creation_request_id_token_signed_response_alg import ClientCreationRequestIdTokenSignedResponseAlg
from .client_creation_request_token_endpoint_auth_method import ClientCreationRequestTokenEndpointAuthMethod
from .organisation_id import OrganisationId


class ClientCreationRequest(UniversalBaseModel):
    additional_software_metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    grant_types: typing.List[str] = pydantic.Field()
    """
    grant_types uri must be provided. For client_credentials this should be array containing ["client_credentials"]
    """

    id_token_signed_response_alg: ClientCreationRequestIdTokenSignedResponseAlg = pydantic.Field()
    """
    Signing algorithim that a client expects the server to return an id_token with. Must be PS256
    """

    jwks_uri: str = pydantic.Field()
    """
    Link to the application active jwks
    """

    organisation_id: OrganisationId
    organisation_name: str
    organisation_number: str = pydantic.Field()
    """
    the cnpj number of the organisation
    """

    redirect_uris: typing.List[str] = pydantic.Field()
    """
    redirect_uris uri must be provided. For client_credentials this should be an empty array.
    """

    response_types: typing.List[str] = pydantic.Field()
    """
    response_types uri must be provided. For client_credentials this should be an empty array
    """

    scope: str = pydantic.Field()
    """
    scopes to be tagged
    """

    software_description: typing.Optional[str] = None
    software_id: typing.Optional[str] = None
    software_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Software Statement client name
    """

    software_roles: typing.List[str] = pydantic.Field()
    """
    array of software roles
    """

    tls_client_auth_subject_dn: typing.Optional[str] = pydantic.Field(default=None)
    """
    The DN of the certificate that will be used to authenticate to this client
    """

    token_endpoint_auth_method: ClientCreationRequestTokenEndpointAuthMethod = pydantic.Field()
    """
    Token endpoint authentication method
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
