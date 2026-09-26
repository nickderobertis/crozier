

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .detail_section_out_id import DetailSectionOutId
from .three_piece_out import ThreePieceOut


class DetailSectionOut(UniversalBaseModel):
    id: DetailSectionOutId
    three_piece: ThreePieceOut

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
