

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_action_run_response_output_item_run_steps_item_name import ListActionRunResponseOutputItemRunStepsItemName
from .list_action_run_response_output_item_run_steps_item_status import (
    ListActionRunResponseOutputItemRunStepsItemStatus,
)


class ListActionRunResponseOutputItemRunStepsItem(UniversalBaseModel):
    name: ListActionRunResponseOutputItemRunStepsItemName
    status: ListActionRunResponseOutputItemRunStepsItemStatus
    created_at: str
    updated_at: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
