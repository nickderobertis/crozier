

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .battle_characters_response_dto_output_characters_item import BattleCharactersResponseDtoOutputCharactersItem


class BattleCharactersResponseDtoOutput(UniversalBaseModel):
    characters: typing.List[BattleCharactersResponseDtoOutputCharactersItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
