

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAuthCodeResponseResponse(UniversalBaseModel):
    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Authorization code. Required to obtain the ID token and / or access token from the /token endpoint.
    """

    redirect_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="redirectUri"),
        pydantic.Field(alias="redirectUri", description="Client's validated redirect URI."),
    ] = None
    """
    Client's validated redirect URI.
    """

    nonce: typing.Optional[str] = pydantic.Field(default=None)
    """
    The echoed nonce value, if one was passed with the request. Clients must validate the value before proceeding.
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    The echoed state value, used to maintain state between the request and the callback.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
