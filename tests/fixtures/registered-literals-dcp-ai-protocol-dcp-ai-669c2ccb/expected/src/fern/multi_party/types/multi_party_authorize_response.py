

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MultiPartyAuthorizeResponse(UniversalBaseModel):
    ok: typing.Optional[bool] = None
    operation: typing.Optional[str] = None
    parties_verified: typing.Optional[int] = None
    threshold_met: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
