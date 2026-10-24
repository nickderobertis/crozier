

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .json_web_key_set import JsonWebKeySet


class Client(UniversalBaseModel):
    """
    The response containing the id and secret of a dynamically registered client.
     Additionally, it contains all registered metadata for the client.
    """

    client_id: str
    client_secret: typing.Optional[str] = None
    client_id_issued_at: typing.Optional[int] = None
    client_secret_expires_at: typing.Optional[int] = None
    redirect_uris: typing.Optional[typing.List[typing.List[str]]] = None
    grant_types: typing.Optional[typing.List[typing.List[str]]] = None
    response_types: typing.Optional[typing.List[typing.List[str]]] = None
    client_name: typing.Optional[str] = None
    client_uri: typing.Optional[str] = None
    logo_uri: typing.Optional[str] = None
    scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    String containing a space-separated list of scope values
     that the client can use when requesting access tokens.
    """

    contacts: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Array of strings representing ways to contact people responsible for this client,
     typically email addresses.
    """

    tos_uri: typing.Optional[str] = None
    policy_uri: typing.Optional[str] = None
    jwks_uri: typing.Optional[str] = None
    jwks: typing.Optional[JsonWebKeySet] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
