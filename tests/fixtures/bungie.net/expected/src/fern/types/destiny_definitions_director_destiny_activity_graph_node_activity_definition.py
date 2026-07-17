

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDirectorDestinyActivityGraphNodeActivityDefinition(UniversalBaseModel):
    """
    The actual activity to be redirected to when you click on the node. Note that a node can have many Activities attached to it: but only one will be active at any given time. The list of Node Activities will be traversed, and the first one found to be active will be displayed. This way, a node can layer multiple variants of an activity on top of each other. For instance, one node can control the weekly Crucible Playlist. There are multiple possible playlists, but only one is active for the week.
    """

    activity_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activityHash"),
        pydantic.Field(
            alias="activityHash",
            description="The activity that will be activated if the user clicks on this node. Controls all activity-related information displayed on the node if it is active (the text shown in the tooltip etc)",
        ),
    ] = None
    """
    The activity that will be activated if the user clicks on this node. Controls all activity-related information displayed on the node if it is active (the text shown in the tooltip etc)
    """

    node_activity_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nodeActivityId"),
        pydantic.Field(
            alias="nodeActivityId",
            description="An identifier for this node activity. It is only guaranteed to be unique within the Activity Graph.",
        ),
    ] = None
    """
    An identifier for this node activity. It is only guaranteed to be unique within the Activity Graph.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
