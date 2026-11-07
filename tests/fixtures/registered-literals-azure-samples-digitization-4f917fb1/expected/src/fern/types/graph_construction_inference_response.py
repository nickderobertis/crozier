

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connected_symbols_item import ConnectedSymbolsItem
from .image_details import ImageDetails


class GraphConstructionInferenceResponse(UniversalBaseModel):
    """
    This class represents the container of connected symbols
    """

    image_url: str
    image_details: ImageDetails
    connected_symbols: typing.List[ConnectedSymbolsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
