

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .hitl_decision_input_action import HitlDecisionInputAction


class HitlDecisionInput(UniversalBaseModel):
    id: str
    action: HitlDecisionInputAction
    edited_args: typing.Optional[typing.Dict[str, typing.Any]] = None
    reject_reason: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
