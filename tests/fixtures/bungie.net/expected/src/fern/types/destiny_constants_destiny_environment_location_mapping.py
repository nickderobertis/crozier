

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyConstantsDestinyEnvironmentLocationMapping(UniversalBaseModel):
    activation_source: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="activationSource"),
        pydantic.Field(
            alias="activationSource",
            description="A hint that the UI uses to figure out how this location is activated by the player.",
        ),
    ] = None
    """
    A hint that the UI uses to figure out how this location is activated by the player.
    """

    activity_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activityHash"),
        pydantic.Field(
            alias="activityHash",
            description="If this is populated, this is the activity you have to be playing in order to see this location appear because of this mapping. (theoretically, a location can have multiple mappings, and some might require you to be in a specific activity when others don't)",
        ),
    ] = None
    """
    If this is populated, this is the activity you have to be playing in order to see this location appear because of this mapping. (theoretically, a location can have multiple mappings, and some might require you to be in a specific activity when others don't)
    """

    item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="itemHash"),
        pydantic.Field(
            alias="itemHash",
            description="If this is populated, it is the item that you must possess for this location to be active because of this mapping. (theoretically, a location can have multiple mappings, and some might require an item while others don't)",
        ),
    ] = None
    """
    If this is populated, it is the item that you must possess for this location to be active because of this mapping. (theoretically, a location can have multiple mappings, and some might require an item while others don't)
    """

    location_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="locationHash"),
        pydantic.Field(
            alias="locationHash", description="The location that is revealed on the director by this mapping."
        ),
    ] = None
    """
    The location that is revealed on the director by this mapping.
    """

    objective_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="objectiveHash"),
        pydantic.Field(
            alias="objectiveHash", description="If this is populated, this is an objective related to the location."
        ),
    ] = None
    """
    If this is populated, this is an objective related to the location.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
