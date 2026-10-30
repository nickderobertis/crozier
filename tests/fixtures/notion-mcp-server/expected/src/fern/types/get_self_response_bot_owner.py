

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_self_response_bot_owner_user import GetSelfResponseBotOwnerUser


class GetSelfResponseBotOwner(UniversalBaseModel):
    type: typing.Optional[str] = None
    user: typing.Optional[GetSelfResponseBotOwnerUser] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
