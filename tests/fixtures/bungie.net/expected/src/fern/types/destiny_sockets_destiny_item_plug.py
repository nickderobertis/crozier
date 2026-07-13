

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_quests_destiny_objective_progress import DestinyQuestsDestinyObjectiveProgress


class DestinySocketsDestinyItemPlug(UniversalBaseModel):
    can_insert: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="canInsert")] = pydantic.Field(
        default=None
    )
    """
    If true, this plug has met all of its insertion requirements. Big if true.
    """

    enable_fail_indexes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="enableFailIndexes")
    ] = pydantic.Field(default=None)
    """
    If a plug is not enabled, this will be populated with indexes into the plug item definition's plug.enabledRules property, so that you can show the reasons why it is not enabled.
    This list will be empty if the plug is enabled.
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, this plug will provide its benefits while inserted.
    """

    insert_fail_indexes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="insertFailIndexes")
    ] = pydantic.Field(default=None)
    """
    If the plug cannot be inserted for some reason, this will have the indexes into the plug item definition's plug.insertionRules property, so you can show the reasons why it can't be inserted.
    This list will be empty if the plug can be inserted.
    """

    plug_item_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="plugItemHash")] = (
        pydantic.Field(default=None)
    )
    """
    The hash identifier of the DestinyInventoryItemDefinition that represents this plug.
    """

    plug_objectives: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyQuestsDestinyObjectiveProgress]], FieldMetadata(alias="plugObjectives")
    ] = pydantic.Field(default=None)
    """
    Sometimes, Plugs may have objectives: these are often used for flavor and display purposes, but they can be used for any arbitrary purpose (both fortunately and unfortunately). Recently (with Season 2) they were expanded in use to be used as the "gating" for whether the plug can be inserted at all. For instance, a Plug might be tracking the number of PVP kills you have made. It will use the parent item's data about that tracking status to determine what to show, and will generally show it using the DestinyObjectiveDefinition's progressDescription property. Refer to the plug's itemHash and objective property for more information if you would like to display even more data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
