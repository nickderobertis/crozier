

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_manifest_config import BaseManifestConfig
from .resource_dependency_types import ResourceDependencyTypes


class ResourceDependency(BaseManifestConfig):
    type: typing.Optional[ResourceDependencyTypes] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
