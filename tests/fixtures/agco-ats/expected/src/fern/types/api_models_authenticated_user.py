

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ApiModelsAuthenticatedUser(UniversalBaseModel):
    email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Email"),
        pydantic.Field(alias="Email", description="The user's email address"),
    ] = None
    """
    The user's email address
    """

    mac_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="MACId"),
        pydantic.Field(alias="MACId", description="The MAC identifier to use for API access"),
    ] = None
    """
    The MAC identifier to use for API access
    """

    mac_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="MACToken"),
        pydantic.Field(alias="MACToken", description="The MAC token to use for API access"),
    ] = None
    """
    The MAC token to use for API access
    """

    name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Name"), pydantic.Field(alias="Name", description="The user's name")
    ] = None
    """
    The user's name
    """

    token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Token"),
        pydantic.Field(alias="Token", description="The token to use for API access"),
    ] = None
    """
    The token to use for API access
    """

    user_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="UserID"), pydantic.Field(alias="UserID", description="The user ID")
    ] = None
    """
    The user ID
    """

    username: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Username"),
        pydantic.Field(alias="Username", description="The username used for authentication"),
    ] = None
    """
    The username used for authentication
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
