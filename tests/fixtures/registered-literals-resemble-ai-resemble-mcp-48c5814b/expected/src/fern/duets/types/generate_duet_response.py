

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .generate_duet_response_item import GenerateDuetResponseItem


class GenerateDuetResponse(UniversalBaseModel):
    success: typing.Optional[bool] = None
    item: typing.Optional[GenerateDuetResponseItem] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
