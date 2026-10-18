

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .open_ai_account_connection_update_params_credentials import OpenAiAccountConnectionUpdateParamsCredentials
from .twilio_account_connection_update_params_credentials import TwilioAccountConnectionUpdateParamsCredentials


class AccountConnectionUpdateParamsRequest_AccountConnectionOpenai(UniversalBaseModel):
    type: typing.Literal["account_connection_openai"] = "account_connection_openai"
    credentials: typing.Optional[OpenAiAccountConnectionUpdateParamsCredentials] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AccountConnectionUpdateParamsRequest_AccountConnectionTwilio(UniversalBaseModel):
    type: typing.Literal["account_connection_twilio"] = "account_connection_twilio"
    credentials: typing.Optional[TwilioAccountConnectionUpdateParamsCredentials] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


AccountConnectionUpdateParamsRequest = typing_extensions.Annotated[
    typing.Union[
        AccountConnectionUpdateParamsRequest_AccountConnectionOpenai,
        AccountConnectionUpdateParamsRequest_AccountConnectionTwilio,
    ],
    pydantic.Field(discriminator="type"),
]
