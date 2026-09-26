

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .generation_output_create_destination_type import GenerationOutputCreateDestinationType
from .generation_output_create_output_kind import GenerationOutputCreateOutputKind


class GenerationOutputCreate(UniversalBaseModel):
    aspect_ratio: typing.Optional[str] = None
    destination_type: typing.Optional[GenerationOutputCreateDestinationType] = None
    height: typing.Optional[int] = None
    marketing_kit_id: typing.Optional[int] = None
    output_key: str
    output_kind: typing.Optional[GenerationOutputCreateOutputKind] = None
    prompt: str
    slot_id: typing.Optional[str] = None
    template_name: typing.Optional[str] = None
    template_ref: str
    width: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
