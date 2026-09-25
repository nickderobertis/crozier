

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OcrSettings(UniversalBaseModel):
    enabled: typing.Optional[bool] = None
    backend: typing.Optional[str] = None
    backend_settings: typing.Optional[typing.Dict[str, typing.Any]] = None
    merge_mode: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
