

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .install_packages_command_source import InstallPackagesCommandSource
from .install_packages_command_type import InstallPackagesCommandType


class InstallPackagesCommand(UniversalBaseModel):
    """
    Install Python packages.

        Installs missing packages using the specified package manager. Triggered
        automatically on import errors or manually by the user.

        Attributes:
            manager: Package manager to use ('pip', 'conda', 'uv', etc.).
            versions: Package names mapped to version specifiers. Empty version
                      means install latest.
            source: Where to install. "kernel" (default) dispatches to the kernel
                    subprocess; "server" installs directly into the server's Python
                    environment (sys.executable), used when the server itself needs
                    a package (e.g. nbformat for IPYNB auto-export in sandbox mode).
    """

    manager: str
    source: typing.Optional[InstallPackagesCommandSource] = None
    type: InstallPackagesCommandType
    versions: typing.Dict[str, str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
