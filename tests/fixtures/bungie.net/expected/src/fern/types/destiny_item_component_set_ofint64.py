

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dictionary_component_response_ofint64and_destiny_item_instance_component import (
    DictionaryComponentResponseOfint64AndDestinyItemInstanceComponent,
)
from .dictionary_component_response_ofint64and_destiny_item_objectives_component import (
    DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent,
)
from .dictionary_component_response_ofint64and_destiny_item_perks_component import (
    DictionaryComponentResponseOfint64AndDestinyItemPerksComponent,
)
from .dictionary_component_response_ofint64and_destiny_item_plug_objectives_component import (
    DictionaryComponentResponseOfint64AndDestinyItemPlugObjectivesComponent,
)
from .dictionary_component_response_ofint64and_destiny_item_render_component import (
    DictionaryComponentResponseOfint64AndDestinyItemRenderComponent,
)
from .dictionary_component_response_ofint64and_destiny_item_reusable_plugs_component import (
    DictionaryComponentResponseOfint64AndDestinyItemReusablePlugsComponent,
)
from .dictionary_component_response_ofint64and_destiny_item_sockets_component import (
    DictionaryComponentResponseOfint64AndDestinyItemSocketsComponent,
)
from .dictionary_component_response_ofint64and_destiny_item_stats_component import (
    DictionaryComponentResponseOfint64AndDestinyItemStatsComponent,
)
from .dictionary_component_response_ofint64and_destiny_item_talent_grid_component import (
    DictionaryComponentResponseOfint64AndDestinyItemTalentGridComponent,
)
from .dictionary_component_response_ofuint32and_destiny_item_plug_component import (
    DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent,
)


class DestinyItemComponentSetOfint64(UniversalBaseModel):
    instances: typing.Optional[DictionaryComponentResponseOfint64AndDestinyItemInstanceComponent] = None
    objectives: typing.Optional[DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent] = None
    perks: typing.Optional[DictionaryComponentResponseOfint64AndDestinyItemPerksComponent] = None
    plug_objectives: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfint64AndDestinyItemPlugObjectivesComponent],
        FieldMetadata(alias="plugObjectives"),
    ] = None
    plug_states: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent],
        FieldMetadata(alias="plugStates"),
    ] = None
    render_data: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfint64AndDestinyItemRenderComponent],
        FieldMetadata(alias="renderData"),
    ] = None
    reusable_plugs: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfint64AndDestinyItemReusablePlugsComponent],
        FieldMetadata(alias="reusablePlugs"),
    ] = None
    sockets: typing.Optional[DictionaryComponentResponseOfint64AndDestinyItemSocketsComponent] = None
    stats: typing.Optional[DictionaryComponentResponseOfint64AndDestinyItemStatsComponent] = None
    talent_grids: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfint64AndDestinyItemTalentGridComponent],
        FieldMetadata(alias="talentGrids"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
