

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .open_ai_account_connection_type import OpenAiAccountConnectionType
from .open_ai_credentials import OpenAiCredentials


class OpenAiAccountConnection(UniversalBaseModel):
    id: str
    user_id: str
    credentials: OpenAiCredentials
    type: OpenAiAccountConnectionType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
