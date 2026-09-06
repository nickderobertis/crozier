

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .interaction_callback_response_resource import InteractionCallbackResponseResource
from .interaction_response import InteractionResponse


class InteractionCallbackResponse(UniversalBaseModel):
    interaction: InteractionResponse
    resource: typing.Optional[InteractionCallbackResponseResource] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
