

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .survey_blocks_item_logic_item_actions_item_calculate import SurveyBlocksItemLogicItemActionsItemCalculate


class SurveyBlocksItemLogicItemActionsItem_Calculate(UniversalBaseModel):
    value: SurveyBlocksItemLogicItemActionsItemCalculate
    objective: typing.Literal["calculate"] = "calculate"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


class SurveyBlocksItemLogicItemActionsItem_RequireAnswer(UniversalBaseModel):
    objective: typing.Literal["requireAnswer"] = "requireAnswer"
    id: str
    target: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SurveyBlocksItemLogicItemActionsItem_JumpToBlock(UniversalBaseModel):
    objective: typing.Literal["jumpToBlock"] = "jumpToBlock"
    id: str
    target: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SurveyBlocksItemLogicItemActionsItem = typing_extensions.Annotated[
    typing.Union[
        SurveyBlocksItemLogicItemActionsItem_Calculate,
        SurveyBlocksItemLogicItemActionsItem_RequireAnswer,
        SurveyBlocksItemLogicItemActionsItem_JumpToBlock,
    ],
    pydantic.Field(discriminator="objective"),
]
