

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GenerationOutputOut(UniversalBaseModel):
    aspect_ratio: typing.Optional[str] = None
    asset_id: typing.Optional[str] = None
    destination_type: str
    error_message: typing.Optional[str] = None
    height: int
    id: str
    image_id: typing.Optional[str] = None
    image_url: typing.Optional[str] = None
    marketing_kit_id: typing.Optional[int] = None
    output_key: str
    output_kind: str
    prompt: str
    slot_id: typing.Optional[str] = None
    sort_order: int
    status: str
    template_name: typing.Optional[str] = None
    template_ref: str
    width: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
