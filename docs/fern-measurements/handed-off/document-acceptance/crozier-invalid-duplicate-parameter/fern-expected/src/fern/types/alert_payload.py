

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .alert_payload_chime import AlertPayloadChime


class AlertPayload(UniversalBaseModel):
    headline: typing.Optional[str] = None
    message: typing.Optional[str] = None
    muted: typing.Optional[bool] = None
    chime: typing.Optional[AlertPayloadChime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
