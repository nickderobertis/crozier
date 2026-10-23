

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .survey_blocks_item_logic_item_actions_item_calculate_zero_value_hidden_field import (
    SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenField,
)


class SurveyBlocksItemLogicItemActionsItemCalculateZeroValue_Static(UniversalBaseModel):
    type: typing.Literal["static"] = "static"
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SurveyBlocksItemLogicItemActionsItemCalculateZeroValue_HiddenField(UniversalBaseModel):
    value: SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenField
    type: typing.Literal["hiddenField"] = "hiddenField"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


SurveyBlocksItemLogicItemActionsItemCalculateZeroValue = typing_extensions.Annotated[
    typing.Union[
        SurveyBlocksItemLogicItemActionsItemCalculateZeroValue_Static,
        SurveyBlocksItemLogicItemActionsItemCalculateZeroValue_HiddenField,
    ],
    pydantic.Field(discriminator="type"),
]
