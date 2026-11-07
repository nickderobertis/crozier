

import typing

from .provider_deployment_state import ProviderDeploymentState
from .unmanaged_state import UnmanagedState

ProviderWithStateState = typing.Union[ProviderDeploymentState, UnmanagedState]
