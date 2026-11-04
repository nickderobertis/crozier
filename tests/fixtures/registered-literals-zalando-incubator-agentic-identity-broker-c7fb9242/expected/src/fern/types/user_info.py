

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UserInfo(UniversalBaseModel):
    principal: str = pydantic.Field()
    """
    User's unique principal identifier from authentication system.
    Typically an email address or UUID.
    """

    display_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="displayName"),
        pydantic.Field(
            alias="displayName",
            description="Human-readable display name for the user.\nUsed in UI for personalization and identification.",
        ),
    ]
    """
    Human-readable display name for the user.
    Used in UI for personalization and identification.
    """

    picture_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pictureUrl"),
        pydantic.Field(
            alias="pictureUrl",
            description="Optional URL to user's profile picture or avatar.\nShould be a publicly accessible HTTPS URL.",
        ),
    ] = None
    """
    Optional URL to user's profile picture or avatar.
    Should be a publicly accessible HTTPS URL.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional email address extracted from JWT claims via CEL expression.
    Only present when JWT pre-authentication is configured with an email_expression and the JWT contains a matching claim. Null/absent when not available.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
