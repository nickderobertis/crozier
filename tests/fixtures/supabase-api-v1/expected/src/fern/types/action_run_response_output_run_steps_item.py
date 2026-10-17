

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_run_response_output_run_steps_item_name import ActionRunResponseOutputRunStepsItemName
from .action_run_response_output_run_steps_item_status import ActionRunResponseOutputRunStepsItemStatus


class ActionRunResponseOutputRunStepsItem(UniversalBaseModel):
    name: ActionRunResponseOutputRunStepsItemName
    status: ActionRunResponseOutputRunStepsItemStatus
    created_at: str
    updated_at: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
