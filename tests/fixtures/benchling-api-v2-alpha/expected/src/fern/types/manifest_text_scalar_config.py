

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_manifest_scalar_config import BaseManifestScalarConfig
from .manifest_text_scalar_config_type import ManifestTextScalarConfigType


class ManifestTextScalarConfig(BaseManifestScalarConfig):
    enum: typing.Optional[typing.List[str]] = None
    type: typing.Optional[ManifestTextScalarConfigType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
