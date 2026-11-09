

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .id import Id
from .tombstone_resource_type import TombstoneResourceType


class Tombstone(UniversalBaseModel):
    """
    A record of a deletion, returned with `410 Gone` when the implementation's top-level `tombstonePolicy` capability is `"410"`. One policy covers RO-Crate, entity and file URIs alike.
    """

    id: Id = pydantic.Field()
    """
    The ID of the deleted resource.
    """

    resource_type: typing_extensions.Annotated[
        TombstoneResourceType,
        FieldMetadata(alias="resourceType"),
        pydantic.Field(alias="resourceType", description="The kind of resource that was deleted."),
    ]
    """
    The kind of resource that was deleted.
    """

    deleted_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="deletedAt"),
        pydantic.Field(alias="deletedAt", description="When the resource was deleted."),
    ]
    """
    When the resource was deleted.
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional human-readable reason for the deletion.
    """

    ro_crate_id: typing_extensions.Annotated[
        typing.Optional[Id],
        FieldMetadata(alias="roCrateId"),
        pydantic.Field(
            alias="roCrateId",
            description="For entity and file tombstones, the RO-Crate whose deletion led to this resource's removal, where known.",
        ),
    ] = None
    """
    For entity and file tombstones, the RO-Crate whose deletion led to this resource's removal, where known.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
