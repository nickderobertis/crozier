

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .entity_access import EntityAccess
from .entity_reference import EntityReference
from .entity_type import EntityType
from .id import Id


class Entity(UniversalBaseModel):
    """
    An entity represents a single collection or item within the repository, conforming to a specific RO-Crate profile.

    For MediaObject entities, the entity `id` is also the file identifier. Use it directly with the `/file/{id}` and `/files` endpoints to access or list the corresponding file.
    """

    id: Id = pydantic.Field()
    """
    RO-Crate ID that uniquely identifies this entity.
    """

    name: str = pydantic.Field()
    """
    Name of the entity.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A concise description of the entity’s contents or purpose.
    """

    entity_type: typing_extensions.Annotated[
        EntityType,
        FieldMetadata(alias="entityType"),
        pydantic.Field(alias="entityType", description="The main classification of the entity"),
    ]
    """
    The main classification of the entity
    """

    member_of: typing_extensions.Annotated[
        typing.Optional[EntityReference],
        FieldMetadata(alias="memberOf"),
        pydantic.Field(alias="memberOf", description="An optional parent entity that this entity belongs to."),
    ] = None
    """
    An optional parent entity that this entity belongs to.
    """

    root_collection: typing_extensions.Annotated[
        typing.Optional[EntityReference],
        FieldMetadata(alias="rootCollection"),
        pydantic.Field(alias="rootCollection", description="The top-level collection this entity is part of."),
    ] = None
    """
    The top-level collection this entity is part of.
    """

    metadata_license_id: typing_extensions.Annotated[
        Id,
        FieldMetadata(alias="metadataLicenseId"),
        pydantic.Field(alias="metadataLicenseId", description="The metadata license."),
    ]
    """
    The metadata license.
    """

    content_license_id: typing_extensions.Annotated[
        Id,
        FieldMetadata(alias="contentLicenseId"),
        pydantic.Field(alias="contentLicenseId", description="The content license."),
    ]
    """
    The content license.
    """

    access: EntityAccess = pydantic.Field()
    """
    Access information for this entity, including permissions and enrolment details.
    """

    ro_crate_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[Id]],
        FieldMetadata(alias="roCrateIds"),
        pydantic.Field(
            alias="roCrateIds",
            description="Optional core — present only when `deposit.supported` is `true`.\n\nThe RO-Crates whose current versions contribute to this entity. Usually one; more when the implementation's materialisation merges contributions from several RO-Crates into a single entity. An entity MAY be removed once no RO-Crate contributes to it.",
        ),
    ] = None
    """
    Optional core — present only when `deposit.supported` is `true`.
    
    The RO-Crates whose current versions contribute to this entity. Usually one; more when the implementation's materialisation merges contributions from several RO-Crates into a single entity. An entity MAY be removed once no RO-Crate contributes to it.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
