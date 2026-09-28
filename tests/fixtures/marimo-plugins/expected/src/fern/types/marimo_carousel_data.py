

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_carousel_data_height import MarimoCarouselDataHeight


class MarimoCarouselData(UniversalBaseModel):
    index: typing.Optional[str] = None
    height: typing.Optional[MarimoCarouselDataHeight] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
