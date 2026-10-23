

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_role import UserRole


class User(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The ID of the user
    """

    created_at: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="The date and time the user was created"),
    ]
    """
    The date and time the user was created
    """

    updated_at: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The date and time the user was last updated"),
    ]
    """
    The date and time the user was last updated
    """

    last_login_at: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="lastLoginAt"),
        pydantic.Field(alias="lastLoginAt", description="The date and time the user last logged in"),
    ]
    """
    The date and time the user last logged in
    """

    is_active: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isActive"),
        pydantic.Field(alias="isActive", description="Whether the user is active"),
    ]
    """
    Whether the user is active
    """

    name: str = pydantic.Field()
    """
    The name of the user
    """

    email: str = pydantic.Field()
    """
    The email of the user
    """

    role: UserRole = pydantic.Field()
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
