

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .channels import Channels
from .response_modalities import ResponseModalities


class FeedbackSettings(UniversalBaseModel):
    modalities: typing.Optional[ResponseModalities] = None
    channels: typing.Optional[Channels] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
