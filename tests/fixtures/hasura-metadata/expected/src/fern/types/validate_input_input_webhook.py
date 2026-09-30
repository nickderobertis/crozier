

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .validate_input_http_definition import ValidateInputHttpDefinition
from .validate_input_input_webhook_type import ValidateInputInputWebhookType


class ValidateInputInputWebhook(UniversalBaseModel):
    definition: ValidateInputHttpDefinition
    type: ValidateInputInputWebhookType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
