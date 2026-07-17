

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_destiny_location_release_definition import DestinyDefinitionsDestinyLocationReleaseDefinition


class DestinyDefinitionsDestinyLocationDefinition(UniversalBaseModel):
    """
    A "Location" is a sort of shortcut for referring to a specific combination of Activity, Destination, Place, and even Bubble or NavPoint within a space.
    Most of this data isn't intrinsically useful to us, but Objectives refer to locations, and through that we can at least infer the Activity, Destination, and Place being referred to by the Objective.
    """

    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    location_releases: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyLocationReleaseDefinition]],
        FieldMetadata(alias="locationReleases"),
        pydantic.Field(
            alias="locationReleases",
            description="A Location may refer to different specific spots in the world based on the world's current state. This is a list of those potential spots, and the data we can use at runtime to determine which one of the spots is the currently valid one.",
        ),
    ] = None
    """
    A Location may refer to different specific spots in the world based on the world's current state. This is a list of those potential spots, and the data we can use at runtime to determine which one of the spots is the currently valid one.
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    vendor_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="vendorHash"),
        pydantic.Field(
            alias="vendorHash",
            description="If the location has a Vendor on it, this is the hash identifier for that Vendor. Look them up with DestinyVendorDefinition.",
        ),
    ] = None
    """
    If the location has a Vendor on it, this is the hash identifier for that Vendor. Look them up with DestinyVendorDefinition.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
