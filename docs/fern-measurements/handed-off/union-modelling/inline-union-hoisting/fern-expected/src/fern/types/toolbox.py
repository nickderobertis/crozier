

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chisel_tool import ChiselTool
from .kit import Kit
from .toolbox_racks import ToolboxRacks
from .toolbox_sets_item import ToolboxSetsItem


class Toolbox(UniversalBaseModel):
    tools: typing.List[ChiselTool]
    kit: typing.Optional[Kit] = None
    spare: typing.Optional[ChiselTool] = None
    racks: typing.Optional[ToolboxRacks] = None
    sets: typing.Optional[typing.List[ToolboxSetsItem]] = None
    labels: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
