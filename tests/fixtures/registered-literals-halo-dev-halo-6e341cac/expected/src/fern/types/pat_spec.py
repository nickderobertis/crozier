

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PatSpec(UniversalBaseModel):
    """
    Desired personal access token settings and lifecycle flags.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional human-readable description of how the token is used.
    """

    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(
            alias="expiresAt",
            description="Time when the token expires. A null value means the token does not expire by time.",
        ),
    ] = None
    """
    Time when the token expires. A null value means the token does not expire by time.
    """

    last_used: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastUsed"),
        pydantic.Field(alias="lastUsed", description="Last time the token was used successfully."),
    ] = None
    """
    Last time the token was used successfully.
    """

    name: str = pydantic.Field()
    """
    Display name chosen by the token owner.
    """

    revoked: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the token has been manually revoked.
    """

    revokes_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="revokesAt"),
        pydantic.Field(alias="revokesAt", description="Time when the token was revoked."),
    ] = None
    """
    Time when the token was revoked.
    """

    roles: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Role names granted to this token.
    """

    scopes: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Scope strings granted to this token.
    """

    token_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="tokenId"),
        pydantic.Field(
            alias="tokenId", description="Stable token identifier stored separately from the secret token value."
        ),
    ]
    """
    Stable token identifier stored separately from the secret token value.
    """

    username: str = pydantic.Field()
    """
    User metadata.name that owns this token.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
