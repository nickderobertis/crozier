

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .generation_plan_item_out_destination_type import GenerationPlanItemOutDestinationType


class GenerationPlanItemOut(UniversalBaseModel):
    aspect_ratio: typing.Optional[str] = None
    destination_type: typing.Optional[GenerationPlanItemOutDestinationType] = None
    enabled: typing.Optional[bool] = None
    id: str
    output_kind: str
    reason: typing.Optional[str] = None
    slot_id: typing.Optional[str] = None
    template_name: typing.Optional[str] = None
    template_ref: typing.Optional[str] = None
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
