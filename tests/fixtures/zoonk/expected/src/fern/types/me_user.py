

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MeUser(UniversalBaseModel):
    analytics_disabled: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="analyticsDisabled"),
        pydantic.Field(
            alias="analyticsDisabled", description="Whether product analytics are disabled for this account"
        ),
    ]
    """
    Whether product analytics are disabled for this account
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="User creation timestamp"),
    ]
    """
    User creation timestamp
    """

    display_username: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayUsername"),
        pydantic.Field(alias="displayUsername", description="Display username"),
    ] = None
    """
    Display username
    """

    email: str = pydantic.Field()
    """
    Email address
    """

    email_verified: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="emailVerified"),
        pydantic.Field(alias="emailVerified", description="Whether the email has been verified"),
    ]
    """
    Whether the email has been verified
    """

    id: str = pydantic.Field()
    """
    User ID
    """

    image: typing.Optional[str] = pydantic.Field(default=None)
    """
    Profile image URL
    """

    name: str = pydantic.Field()
    """
    Display name
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="User update timestamp"),
    ]
    """
    User update timestamp
    """

    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    Normalized username
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
