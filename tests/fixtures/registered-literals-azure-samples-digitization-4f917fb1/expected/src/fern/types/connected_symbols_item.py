

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bounding_box import BoundingBox
from .connected_symbols_connection_item import ConnectedSymbolsConnectionItem


class ConnectedSymbolsItem(UniversalBaseModel):
    """
    This class represents a symbol that is connected to other symbols
    """

    id: int
    label: str
    text_associated: str
    bounding_box: BoundingBox
    connections: typing.List[ConnectedSymbolsConnectionItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
