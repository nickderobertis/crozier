

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_action_run_response_output_item_run_steps_item import ListActionRunResponseOutputItemRunStepsItem


class ListActionRunResponseOutputItem(UniversalBaseModel):
    id: str
    branch_id: str
    run_steps: typing.List[ListActionRunResponseOutputItemRunStepsItem]
    git_config: typing.Optional[typing.Any] = None
    workdir: typing.Optional[str] = None
    check_run_id: typing.Optional[float] = None
    created_at: str
    updated_at: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
