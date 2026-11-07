

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bounding_box import BoundingBox
from .image_details import ImageDetails
from .label import Label


class SymbolDetectionInferenceResponse(UniversalBaseModel):
    """
    This class represents the symbol detection inference results; which includes
    all symbols detected, and the symbols and text associated on a P&ID image.
    """

    image_url: str
    image_details: ImageDetails
    bounding_box_inclusive: typing.Optional[BoundingBox] = None
    label: typing.List[Label]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
