

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .revocation_request_token_type_hint import RevocationRequestTokenTypeHint


class RevocationRequest(UniversalBaseModel):
    token: str
    token_type_hint: typing.Optional[RevocationRequestTokenTypeHint] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
