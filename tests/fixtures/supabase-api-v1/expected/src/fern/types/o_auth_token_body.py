

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .o_auth_token_body_grant_type import OAuthTokenBodyGrantType


class OAuthTokenBody(UniversalBaseModel):
    grant_type: typing.Optional[OAuthTokenBodyGrantType] = None
    client_id: typing.Optional[str] = None
    client_secret: typing.Optional[str] = None
    code: typing.Optional[str] = None
    code_verifier: typing.Optional[str] = None
    redirect_uri: typing.Optional[str] = None
    refresh_token: typing.Optional[str] = None
    assertion: typing.Optional[str] = pydantic.Field(default=None)
    """
    IDJAG assertion JWT for grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer. Beta - available on Team and Enterprise plans only.
    """

    resource: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resource indicator for MCP (Model Context Protocol) clients
    """

    scope: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
