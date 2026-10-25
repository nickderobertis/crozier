

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetMeResponse(UniversalBaseModel):
    sub: typing.Optional[str] = None
    email: typing.Optional[str] = None
    email_verified: typing.Optional[bool] = None
    name: typing.Optional[str] = None
    picture: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
