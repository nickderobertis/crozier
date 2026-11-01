

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StrataGetAuthResponse(UniversalBaseModel):
    success: bool
    server_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="serverName"), pydantic.Field(alias="serverName", description="The name of the server")
    ]
    """
    The name of the server
    """

    auth_data: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="authData"),
        pydantic.Field(alias="authData", description="The authentication data if available"),
    ] = None
    """
    The authentication data if available
    """

    is_authenticated: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isAuthenticated"),
        pydantic.Field(alias="isAuthenticated", description="Whether the server has authentication data configured"),
    ]
    """
    Whether the server has authentication data configured
    """

    message: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
