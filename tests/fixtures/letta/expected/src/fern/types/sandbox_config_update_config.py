

import typing

from .e2b_sandbox_config import E2BSandboxConfig
from .local_sandbox_config import LocalSandboxConfig
from .modal_sandbox_config import ModalSandboxConfig

SandboxConfigUpdateConfig = typing.Union[LocalSandboxConfig, E2BSandboxConfig, ModalSandboxConfig]
