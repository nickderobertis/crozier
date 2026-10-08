

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .environment_variable_discovery_value_kind import EnvironmentVariableDiscoveryValueKind


class EnvironmentVariableDiscoveryValue(UniversalBaseModel):
    """
    A reference to an environment variable, never its value.
    """

    kind: EnvironmentVariableDiscoveryValueKind
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
