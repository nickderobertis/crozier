

import typing

from .provider_deployment_state import ProviderDeploymentState
from .unmanaged_state import UnmanagedState

AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2State = typing.Union[
    ProviderDeploymentState, UnmanagedState
]
