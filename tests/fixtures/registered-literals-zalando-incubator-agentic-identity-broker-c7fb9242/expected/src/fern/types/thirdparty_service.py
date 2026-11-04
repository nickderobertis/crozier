

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .service_scope import ServiceScope


class ThirdpartyService(UniversalBaseModel):
    service_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="serviceId"),
        pydantic.Field(
            alias="serviceId",
            description="Unique service identifier (UUID).\nUsed in grant requests to specify which service to delegate.",
        ),
    ]
    """
    Unique service identifier (UUID).
    Used in grant requests to specify which service to delegate.
    """

    display_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Human-readable service name"),
    ]
    """
    Human-readable service name
    """

    logo_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="logoUrl"),
        pydantic.Field(alias="logoUrl", description="Optional URL to service's logo or icon"),
    ] = None
    """
    Optional URL to service's logo or icon
    """

    scopes: typing.List[ServiceScope] = pydantic.Field()
    """
    Array of available scopes for this service.
    Users select which scopes to grant when creating a delegation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
