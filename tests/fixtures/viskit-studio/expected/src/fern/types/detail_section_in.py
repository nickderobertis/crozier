

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .detail_section_in_id import DetailSectionInId
from .three_piece_in import ThreePieceIn


class DetailSectionIn(UniversalBaseModel):
    id: DetailSectionInId
    three_piece: ThreePieceIn

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
