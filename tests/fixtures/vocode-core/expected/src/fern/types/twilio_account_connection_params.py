

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .twilio_credentials import TwilioCredentials


class TwilioAccountConnectionParams(UniversalBaseModel):
    credentials: TwilioCredentials
    steering_pool: typing.Optional[typing.List[str]] = None
    account_supports_any_caller_id: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
