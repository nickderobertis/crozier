

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .package_management_config_manager import PackageManagementConfigManager


class PackageManagementConfig(UniversalBaseModel):
    """
    Configuration options for package management.

        **Keys.**

        - `manager`: the package manager to use
    """

    manager: PackageManagementConfigManager

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
