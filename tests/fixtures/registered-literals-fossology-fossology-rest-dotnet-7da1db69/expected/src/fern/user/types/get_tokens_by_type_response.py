

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...types.info import Info
from ...types.token import Token


class GetTokensByTypeResponse(Info):
    active_tokens: typing.Optional[Token] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
