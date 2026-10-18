

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .external_action_config_processing_mode import ExternalActionConfigProcessingMode


class ExternalActionConfig(UniversalBaseModel):
    processing_mode: typing.Optional[ExternalActionConfigProcessingMode] = None
    name: str
    description: str
    url: str
    input_schema: typing.Dict[str, typing.Any]
    speak_on_send: bool
    speak_on_receive: bool
    signature_secret: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
