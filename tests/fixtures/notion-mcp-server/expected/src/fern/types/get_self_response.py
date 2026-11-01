

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_self_response_bot import GetSelfResponseBot


class GetSelfResponse(UniversalBaseModel):
    object: typing.Optional[str] = None
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    avatar_url: typing.Optional[typing.Any] = None
    type: typing.Optional[str] = None
    bot: typing.Optional[GetSelfResponseBot] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
