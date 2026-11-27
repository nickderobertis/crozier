

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_manifest_scalar_config import BaseManifestScalarConfig
from .manifest_integer_scalar_config_type import ManifestIntegerScalarConfigType


class ManifestIntegerScalarConfig(BaseManifestScalarConfig):
    enum: typing.Optional[typing.List[int]] = None
    type: typing.Optional[ManifestIntegerScalarConfigType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
