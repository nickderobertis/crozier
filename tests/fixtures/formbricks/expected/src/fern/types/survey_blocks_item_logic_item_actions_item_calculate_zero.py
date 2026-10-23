

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .survey_blocks_item_logic_item_actions_item_calculate_zero_objective import (
    SurveyBlocksItemLogicItemActionsItemCalculateZeroObjective,
)
from .survey_blocks_item_logic_item_actions_item_calculate_zero_operator import (
    SurveyBlocksItemLogicItemActionsItemCalculateZeroOperator,
)
from .survey_blocks_item_logic_item_actions_item_calculate_zero_value import (
    SurveyBlocksItemLogicItemActionsItemCalculateZeroValue,
)


class SurveyBlocksItemLogicItemActionsItemCalculateZero(UniversalBaseModel):
    id: str
    objective: SurveyBlocksItemLogicItemActionsItemCalculateZeroObjective
    variable_id: typing_extensions.Annotated[str, FieldMetadata(alias="variableId"), pydantic.Field(alias="variableId")]
    operator: SurveyBlocksItemLogicItemActionsItemCalculateZeroOperator
    value: SurveyBlocksItemLogicItemActionsItemCalculateZeroValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
