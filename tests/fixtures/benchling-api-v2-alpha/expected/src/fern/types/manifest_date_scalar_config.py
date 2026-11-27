

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_manifest_scalar_config import BaseManifestScalarConfig
from .manifest_date_scalar_config_type import ManifestDateScalarConfigType


class ManifestDateScalarConfig(BaseManifestScalarConfig):
    type: typing.Optional[ManifestDateScalarConfigType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
