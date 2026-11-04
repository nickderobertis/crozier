

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_links import UserLinks
from .user_type import UserType


class User(UniversalBaseModel):
    """
    User object
    """

    id: str = pydantic.Field()
    """
    The ID of this user
    """

    type: UserType = pydantic.Field()
    """
    Whether this is a user or an organization
    """

    bio: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user’s biography, if they have provided one
    """

    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user’s handle that they chose for themselves. Does not include the @ symbol
    """

    profile_image_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="profileImageUrl"),
        pydantic.Field(
            alias="profileImageUrl", description="URL that points to the user’s profile image, if one exists"
        ),
    ] = None
    """
    URL that points to the user’s profile image, if one exists
    """

    url: str = pydantic.Field()
    """
    URL of this user’s profile on Val Town’s website
    """

    links: UserLinks

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
