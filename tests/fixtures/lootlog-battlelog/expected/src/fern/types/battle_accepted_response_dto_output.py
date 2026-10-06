

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .battle_accepted_response_dto_output_status import BattleAcceptedResponseDtoOutputStatus


class BattleAcceptedResponseDtoOutput(UniversalBaseModel):
    status: BattleAcceptedResponseDtoOutputStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
