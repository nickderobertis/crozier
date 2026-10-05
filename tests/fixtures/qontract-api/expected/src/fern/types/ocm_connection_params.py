

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OcmConnectionParams(UniversalBaseModel):
    """
    OCM environment connection details, shared by every OCM-backed integration.

    Deliberately generic - carries no notion of "rhidp" or any other consumer. The
    inherited Secret fields (secret_manager_url, path, field, version) resolve
    access_token_client_secret.
    """

    access_token_client_id: str = pydantic.Field()
    """
    OAuth2 client id
    """

    access_token_url: str = pydantic.Field()
    """
    OAuth2 token endpoint (client-credentials grant)
    """

    field: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specific field within the secret
    """

    ocm_url: str = pydantic.Field()
    """
    OCM environment base URL
    """

    path: str = pydantic.Field()
    """
    Path to the secret
    """

    secret_manager_url: str = pydantic.Field()
    """
    Secret Manager URL
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version of the secret
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
