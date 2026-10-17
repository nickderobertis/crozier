

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .open_ai_credentials import OpenAiCredentials
from .twilio_credentials import TwilioCredentials


class AccountConnectionPageItemsItem_AccountConnectionOpenai(UniversalBaseModel):
    type: typing.Literal["account_connection_openai"] = "account_connection_openai"
    id: str
    user_id: str
    credentials: OpenAiCredentials

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AccountConnectionPageItemsItem_AccountConnectionTwilio(UniversalBaseModel):
    type: typing.Literal["account_connection_twilio"] = "account_connection_twilio"
    id: str
    user_id: str
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


AccountConnectionPageItemsItem = typing_extensions.Annotated[
    typing.Union[
        AccountConnectionPageItemsItem_AccountConnectionOpenai, AccountConnectionPageItemsItem_AccountConnectionTwilio
    ],
    pydantic.Field(discriminator="type"),
]
