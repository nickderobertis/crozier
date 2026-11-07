

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .scalar_defaults_mode import ScalarDefaultsMode


class ScalarDefaults(UniversalBaseModel):
    enabled: typing.Optional[bool] = None
    retries: typing.Optional[int] = None
    sequence: typing.Optional[int] = None
    ratio: typing.Optional[float] = None
    threshold: typing.Optional[float] = None
    label: typing.Optional[str] = None
    mode: typing.Optional[ScalarDefaultsMode] = None
    nullable_label: typing.Optional[str] = None
    nullable_fallback: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
