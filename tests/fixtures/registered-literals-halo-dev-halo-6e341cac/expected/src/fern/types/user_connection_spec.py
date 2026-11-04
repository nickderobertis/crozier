

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UserConnectionSpec(UniversalBaseModel):
    """
    External OAuth2 account binding for a Halo user.
    """

    provider_user_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="providerUserId"),
        pydantic.Field(
            alias="providerUserId",
            description="The unique identifier for the user's connection to the OAuth provider. for example, the user's GitHub id.",
        ),
    ]
    """
    The unique identifier for the user's connection to the OAuth provider. for example, the user's GitHub id.
    """

    registration_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="registrationId"),
        pydantic.Field(
            alias="registrationId", description="The name of the OAuth provider (e.g. Google, Facebook, Twitter)."
        ),
    ]
    """
    The name of the OAuth provider (e.g. Google, Facebook, Twitter).
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The time when the user connection was last updated."),
    ] = None
    """
    The time when the user connection was last updated.
    """

    username: str = pydantic.Field()
    """
    The {@link Metadata#getName Metadata#getName()} of the user associated with the OAuth connection.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
