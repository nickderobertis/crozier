

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .generation_plan_item_out import GenerationPlanItemOut
from .generation_plan_out_plan_source import GenerationPlanOutPlanSource


class GenerationPlanOut(UniversalBaseModel):
    items: typing.List[GenerationPlanItemOut]
    plan_id: str
    plan_source: GenerationPlanOutPlanSource
    planner_note: typing.Optional[str] = None
    planner_payload: typing.Optional[typing.Dict[str, typing.Any]] = None
    requires_confirmation: bool
    source_image_ref: str
    user_prompt: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
