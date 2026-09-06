

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ApiModelsUser(UniversalBaseModel):
    change_password: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ChangePassword"),
        pydantic.Field(
            alias="ChangePassword",
            description="Never Returned.  When changing a user's password, this field must contain the new password.",
        ),
    ] = None
    """
    Never Returned.  When changing a user's password, this field must contain the new password.
    """

    email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Email"),
        pydantic.Field(alias="Email", description="The user's email address"),
    ] = None
    """
    The user's email address
    """

    name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Name"), pydantic.Field(alias="Name", description="The user's name")
    ] = None
    """
    The user's name
    """

    password: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Password"),
        pydantic.Field(
            alias="Password",
            description="Never Returned.  Required when creating a new user or updating a user.  When changing a user's password this field must contain the current password.",
        ),
    ] = None
    """
    Never Returned.  Required when creating a new user or updating a user.  When changing a user's password this field must contain the current password.
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
