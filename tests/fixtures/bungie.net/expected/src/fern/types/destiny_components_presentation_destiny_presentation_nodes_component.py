

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_components_presentation_destiny_presentation_node_component import (
    DestinyComponentsPresentationDestinyPresentationNodeComponent,
)


class DestinyComponentsPresentationDestinyPresentationNodesComponent(UniversalBaseModel):
    nodes: typing.Optional[typing.Dict[str, DestinyComponentsPresentationDestinyPresentationNodeComponent]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
