

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_manifest_scalar_config import BaseManifestScalarConfig
from .manifest_float_scalar_config_type import ManifestFloatScalarConfigType


class ManifestFloatScalarConfig(BaseManifestScalarConfig):
    enum: typing.Optional[typing.List[float]] = None
    type: typing.Optional[ManifestFloatScalarConfigType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
