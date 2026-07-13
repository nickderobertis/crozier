

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dictionary_component_response_ofuint32and_destiny_item_instance_component import (
    DictionaryComponentResponseOfuint32AndDestinyItemInstanceComponent,
)
from .dictionary_component_response_ofuint32and_destiny_item_objectives_component import (
    DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent,
)
from .dictionary_component_response_ofuint32and_destiny_item_perks_component import (
    DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent,
)
from .dictionary_component_response_ofuint32and_destiny_item_plug_component import (
    DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent,
)
from .dictionary_component_response_ofuint32and_destiny_item_plug_objectives_component import (
    DictionaryComponentResponseOfuint32AndDestinyItemPlugObjectivesComponent,
)
from .dictionary_component_response_ofuint32and_destiny_item_render_component import (
    DictionaryComponentResponseOfuint32AndDestinyItemRenderComponent,
)
from .dictionary_component_response_ofuint32and_destiny_item_reusable_plugs_component import (
    DictionaryComponentResponseOfuint32AndDestinyItemReusablePlugsComponent,
)
from .dictionary_component_response_ofuint32and_destiny_item_sockets_component import (
    DictionaryComponentResponseOfuint32AndDestinyItemSocketsComponent,
)
from .dictionary_component_response_ofuint32and_destiny_item_stats_component import (
    DictionaryComponentResponseOfuint32AndDestinyItemStatsComponent,
)
from .dictionary_component_response_ofuint32and_destiny_item_talent_grid_component import (
    DictionaryComponentResponseOfuint32AndDestinyItemTalentGridComponent,
)


class DestinyItemComponentSetOfuint32(UniversalBaseModel):
    instances: typing.Optional[DictionaryComponentResponseOfuint32AndDestinyItemInstanceComponent] = None
    objectives: typing.Optional[DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent] = None
    perks: typing.Optional[DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent] = None
    plug_objectives: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfuint32AndDestinyItemPlugObjectivesComponent],
        FieldMetadata(alias="plugObjectives"),
    ] = None
    plug_states: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent],
        FieldMetadata(alias="plugStates"),
    ] = None
    render_data: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfuint32AndDestinyItemRenderComponent],
        FieldMetadata(alias="renderData"),
    ] = None
    reusable_plugs: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfuint32AndDestinyItemReusablePlugsComponent],
        FieldMetadata(alias="reusablePlugs"),
    ] = None
    sockets: typing.Optional[DictionaryComponentResponseOfuint32AndDestinyItemSocketsComponent] = None
    stats: typing.Optional[DictionaryComponentResponseOfuint32AndDestinyItemStatsComponent] = None
    talent_grids: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfuint32AndDestinyItemTalentGridComponent],
        FieldMetadata(alias="talentGrids"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
