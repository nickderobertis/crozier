

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)


class DestinyDefinitionsChecklistsDestinyChecklistEntryDefinition(UniversalBaseModel):
    """
    The properties of an individual checklist item. Note that almost everything is optional: it is *highly* variable what kind of data we'll actually be able to return: at times we may have no other relationships to entities at all.
    Whatever UI you build, do it with the knowledge that any given entry might not actually be able to be associated with some other Destiny entity.
    """

    activity_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="activityHash")] = None
    bubble_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="bubbleHash")] = pydantic.Field(
        default=None
    )
    """
    Note that a Bubble's hash doesn't uniquely identify a "top level" entity in Destiny. Only the combination of location and bubble can uniquely identify a place in the world of Destiny: so if bubbleHash is populated, locationHash must too be populated for it to have any meaning.
    You can use this property if it is populated to look up the DestinyLocationDefinition's associated .locationReleases[].activityBubbleName property.
    """

    destination_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="destinationHash")] = None
    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
    ] = pydantic.Field(default=None)
    """
    Even if no other associations exist, we will give you *something* for display properties. In cases where we have no associated entities, it may be as simple as a numerical identifier.
    """

    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The identifier for this Checklist entry. Guaranteed unique only within this Checklist Definition, and not globally/for all checklists.
    """

    item_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="itemHash")] = None
    location_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="locationHash")] = None
    scope: typing.Optional[int] = pydantic.Field(default=None)
    """
    The scope at which this specific entry can be computed.
    """

    vendor_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="vendorHash")] = None
    vendor_interaction_index: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="vendorInteractionIndex")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
