

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WebhookSettings(UniversalBaseModel):
    disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Flag indicating if the webhook is disabled
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Webhook ID
    """

    transform: typing.Optional[str] = pydantic.Field(default=None)
    """
    Transformation to be applied to the event
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
