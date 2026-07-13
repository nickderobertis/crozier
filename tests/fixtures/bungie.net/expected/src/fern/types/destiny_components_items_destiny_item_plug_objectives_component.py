

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_quests_destiny_objective_progress import DestinyQuestsDestinyObjectiveProgress


class DestinyComponentsItemsDestinyItemPlugObjectivesComponent(UniversalBaseModel):
    objectives_per_plug: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.List[DestinyQuestsDestinyObjectiveProgress]]],
        FieldMetadata(alias="objectivesPerPlug"),
    ] = pydantic.Field(default=None)
    """
    This set of data is keyed by the Item Hash (DestinyInventoryItemDefinition) of the plug whose objectives are being returned, with the value being the list of those objectives.
     What if two plugs with the same hash are returned for an item, you ask?
     Good question! They share the same item-scoped state, and as such would have identical objective state as a result. How's that for convenient.
     Sometimes, Plugs may have objectives: generally, these are used for flavor and display purposes. For instance, a Plug might be tracking the number of PVP kills you have made. It will use the parent item's data about that tracking status to determine what to show, and will generally show it using the DestinyObjectiveDefinition's progressDescription property. Refer to the plug's itemHash and objective property for more information if you would like to display even more data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
