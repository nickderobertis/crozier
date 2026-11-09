

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bounding_box import BoundingBox
from .image_details import ImageDetails
from .symbol_and_text_associated import SymbolAndTextAssociated
from .text_recognized import TextRecognized


class TextDetectionInferenceResponse(UniversalBaseModel):
    """
    This class represents the text detection inference results; which includes
    all text detected, and the text and symbols associated on a P&ID image.
    """

    image_url: str
    image_details: ImageDetails
    bounding_box_inclusive: typing.Optional[BoundingBox] = None
    all_text_list: typing.List[TextRecognized]
    text_and_symbols_associated_list: typing.List[SymbolAndTextAssociated]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
