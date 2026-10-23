

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PatchWebhooksIdResponseWebhookOne(UniversalBaseModel):
    id: str
    name: str
    url: str
    secret_prefix: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="secretPrefix"),
        pydantic.Field(
            alias="secretPrefix",
            description="The first characters of the signing secret; the secret itself is returned only once, at creation or rotation.",
        ),
    ]
    """
    The first characters of the signing secret; the secret itself is returned only once, at creation or rotation.
    """

    enabled: bool
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    last_delivered_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastDeliveredAt"),
        pydantic.Field(
            alias="lastDeliveredAt",
            description="When this endpoint last answered 2xx, including test pings — not necessarily an alert.",
        ),
    ] = None
    """
    When this endpoint last answered 2xx, including test pings — not necessarily an alert.
    """

    last_error: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastError"),
        pydantic.Field(
            alias="lastError",
            description="The most recent failure whenever it happened, cleared by the next success. Compare lastErrorAt with lastDeliveredAt before reading it as a fault now.",
        ),
    ] = None
    """
    The most recent failure whenever it happened, cleared by the next success. Compare lastErrorAt with lastDeliveredAt before reading it as a fault now.
    """

    last_error_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastErrorAt"),
        pydantic.Field(
            alias="lastErrorAt",
            description="When lastError was written. Null on an endpoint whose last failure predates this field.",
        ),
    ] = None
    """
    When lastError was written. Null on an endpoint whose last failure predates this field.
    """

    secret: str = pydantic.Field()
    """
    Present only in the response that created or rotated this endpoint. Stored encrypted and never returned again.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
