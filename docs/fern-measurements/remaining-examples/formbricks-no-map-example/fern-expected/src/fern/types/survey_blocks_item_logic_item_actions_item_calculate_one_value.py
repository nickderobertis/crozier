

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .survey_blocks_item_logic_item_actions_item_calculate_one_value_hidden_field import (
    SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenField,
)


class SurveyBlocksItemLogicItemActionsItemCalculateOneValue_Static(UniversalBaseModel):
    type: typing.Literal["static"] = "static"
    value: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SurveyBlocksItemLogicItemActionsItemCalculateOneValue_HiddenField(UniversalBaseModel):
    value: SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenField
    type: typing.Literal["hiddenField"] = "hiddenField"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


SurveyBlocksItemLogicItemActionsItemCalculateOneValue = typing_extensions.Annotated[
    typing.Union[
        SurveyBlocksItemLogicItemActionsItemCalculateOneValue_Static,
        SurveyBlocksItemLogicItemActionsItemCalculateOneValue_HiddenField,
    ],
    pydantic.Field(discriminator="type"),
]
