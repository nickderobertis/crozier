

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TokenResponse(UniversalBaseModel):
    """
    A signed JWT token when used in the context of a dummy token. Otherwise, a signed JWT access token and a signed JWE refresh token.
    """

    token: typing.Optional[str] = pydantic.Field(default=None)
    """
    A dummy token
    """

    refresh_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="refreshToken"),
        pydantic.Field(alias="refreshToken", description="A refresh token"),
    ] = None
    """
    A refresh token
    """

    access_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="accessToken"),
        pydantic.Field(alias="accessToken", description="An access token"),
    ] = None
    """
    An access token
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
