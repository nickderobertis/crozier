

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_manifest_config import BaseManifestConfig
from .dropdown_dependency_types import DropdownDependencyTypes


class DropdownDependency(BaseManifestConfig):
    options: typing.Optional[typing.List[BaseManifestConfig]] = None
    type: typing.Optional[DropdownDependencyTypes] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
