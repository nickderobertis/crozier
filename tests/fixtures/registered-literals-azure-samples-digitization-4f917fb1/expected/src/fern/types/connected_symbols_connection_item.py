

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bounding_box import BoundingBox
from .flow_direction import FlowDirection


class ConnectedSymbolsConnectionItem(UniversalBaseModel):
    """
    This class represents a symbol that is connected to other symbols
    """

    id: int
    label: str
    text_associated: str
    bounding_box: BoundingBox
    flow_direction: FlowDirection
    segments: typing.List[BoundingBox]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
