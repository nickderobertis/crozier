

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetAuthDataResponse(UniversalBaseModel):
    success: bool = pydantic.Field()
    """
    Whether the request was successful
    """

    auth_data: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="authData"),
        pydantic.Field(
            alias="authData",
            description="Complete authentication data including access token, refresh token, scope, expiration, and platform-specific data",
        ),
    ] = None
    """
    Complete authentication data including access token, refresh token, scope, expiration, and platform-specific data
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error message if the request failed
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
