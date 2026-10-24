

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pilot_open_ai_component_status import PilotOpenAiComponentStatus


class PilotOpenAiComponent(UniversalBaseModel):
    """
    Presence flags only; no OpenAI credential or model value is returned.
    """

    required: bool
    status: PilotOpenAiComponentStatus
    api_key_present: bool
    model_present: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
