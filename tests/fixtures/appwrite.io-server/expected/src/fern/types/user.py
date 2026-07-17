

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class User(UniversalBaseModel):
    """
    User
    """

    id: typing_extensions.Annotated[
        str, FieldMetadata(alias="$id"), pydantic.Field(alias="$id", description="User ID.")
    ]
    """
    User ID.
    """

    email: str = pydantic.Field()
    """
    User email address.
    """

    email_verification: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="emailVerification"),
        pydantic.Field(alias="emailVerification", description="Email verification status."),
    ]
    """
    Email verification status.
    """

    name: str = pydantic.Field()
    """
    User name.
    """

    password_update: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="passwordUpdate"),
        pydantic.Field(alias="passwordUpdate", description="Unix timestamp of the most recent password update"),
    ]
    """
    Unix timestamp of the most recent password update
    """

    prefs: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    User preferences as a key-value object
    """

    registration: int = pydantic.Field()
    """
    User registration date in Unix timestamp.
    """

    status: int = pydantic.Field()
    """
    User status. 0 for Unactivated, 1 for active and 2 is blocked.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
