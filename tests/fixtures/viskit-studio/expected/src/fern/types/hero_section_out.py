

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .hero_section_out_id import HeroSectionOutId
from .three_piece_out import ThreePieceOut


class HeroSectionOut(UniversalBaseModel):
    id: HeroSectionOutId
    three_piece: ThreePieceOut

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
