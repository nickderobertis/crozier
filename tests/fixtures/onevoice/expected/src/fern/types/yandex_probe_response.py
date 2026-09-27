

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class YandexProbeResponse(UniversalBaseModel):
    ok: bool
    format: typing.Optional[str] = None
    session_valid: typing.Optional[bool] = None
    username: typing.Optional[str] = None
    warnings: typing.Optional[typing.List[str]] = None
    error: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
