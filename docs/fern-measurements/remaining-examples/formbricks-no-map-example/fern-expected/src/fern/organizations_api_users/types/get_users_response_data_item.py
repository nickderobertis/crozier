

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_users_response_data_item_role import GetUsersResponseDataItemRole


class GetUsersResponseDataItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the user
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="The date and time the user was created"),
    ] = None
    """
    The date and time the user was created
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The date and time the user was last updated"),
    ] = None
    """
    The date and time the user was last updated
    """

    last_login_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastLoginAt"),
        pydantic.Field(alias="lastLoginAt", description="The date and time the user last logged in"),
    ] = None
    """
    The date and time the user last logged in
    """

    is_active: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isActive"),
        pydantic.Field(alias="isActive", description="Whether the user is active"),
    ] = None
    """
    Whether the user is active
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the user
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email of the user
    """

    role: typing.Optional[GetUsersResponseDataItemRole] = pydantic.Field(default=None)
    """
    The role of the user in the organization
    """

    teams: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The list of teams the user is a member of
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
