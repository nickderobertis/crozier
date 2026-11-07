

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_key_kind import ApiKeyKind


class ApiKey(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Stable non-secret identifier for the API key.
    """

    name: str = pydantic.Field()
    """
    Human-readable key name supplied at creation.
    """

    prefix: str = pydantic.Field()
    """
    Non-secret prefix you can use to identify the key in logs and settings.
    """

    scopes: typing.List[str] = pydantic.Field()
    """
    Permissions granted to the key. Every API operation still enforces its required scope.
    """

    request_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="requestCount"),
        pydantic.Field(alias="requestCount", description="Lifetime number of requests authenticated with this key."),
    ]
    """
    Lifetime number of requests authenticated with this key.
    """

    last_used_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastUsedAt"),
        pydantic.Field(
            alias="lastUsedAt",
            description="When Darwin most recently authenticated a request with this key, or null if unused.",
        ),
    ] = None
    """
    When Darwin most recently authenticated a request with this key, or null if unused.
    """

    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(
            alias="expiresAt", description="When the key expires, or null when it has no scheduled expiration."
        ),
    ] = None
    """
    When the key expires, or null when it has no scheduled expiration.
    """

    revoked_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="revokedAt"),
        pydantic.Field(
            alias="revokedAt", description="When the key was revoked, or null while it has not been revoked."
        ),
    ] = None
    """
    When the key was revoked, or null while it has not been revoked.
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="When the key was created."),
    ]
    """
    When the key was created.
    """

    kind: typing.Optional[ApiKeyKind] = pydantic.Field(default=None)
    """
    New keys identify an application; legacy keys retain their previous user-bound behavior until revoked.
    """

    application_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="applicationId"),
        pydantic.Field(
            alias="applicationId", description="The application identified by a new key, or null for a legacy user key."
        ),
    ] = None
    """
    The application identified by a new key, or null for a legacy user key.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
