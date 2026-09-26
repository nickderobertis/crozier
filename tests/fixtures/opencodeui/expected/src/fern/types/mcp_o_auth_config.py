

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class McpOAuthConfig(UniversalBaseModel):
    client_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="clientId"),
        pydantic.Field(
            alias="clientId",
            description="OAuth client ID. If not provided, dynamic client registration (RFC 7591) will be attempted.",
        ),
    ] = None
    """
    OAuth client ID. If not provided, dynamic client registration (RFC 7591) will be attempted.
    """

    client_secret: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="clientSecret"),
        pydantic.Field(
            alias="clientSecret", description="OAuth client secret (if required by the authorization server)"
        ),
    ] = None
    """
    OAuth client secret (if required by the authorization server)
    """

    scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    OAuth scopes to request during authorization
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
